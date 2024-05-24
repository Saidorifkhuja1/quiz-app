from django.shortcuts import get_object_or_404, redirect,render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Exam, Quiz


class HomeTeacherPageView(TemplateView):
    template_name = 'home.html'



class ExamCreateView(UserPassesTestMixin, CreateView):
    model = Exam
    template_name = 'exam_create.html'
    fields = ('title', 'description', 'start_date', 'end_date', 'time_limit_minutes')
    success_url = reverse_lazy('exam_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class ExanListView(ListView):
    model = Exam
    template_name = 'exam_list.html'
    context_object_name = 'exams'

    def get_queryset(self):
        return Exam.objects.prefetch_related('quizzes')

class ExamDetailView(DetailView):
    model = Exam
    template_name = 'exam_detail.html'

class QuizCreateView(CreateView,UserPassesTestMixin):
    model = Quiz
    template_name = 'quiz_create.html'
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_option']

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.are_you_teacher

    def get_success_url(self):

        exam_id = self.kwargs.get('exam_id')
        return reverse_lazy('exam_detail', kwargs={'pk': exam_id})

    def form_valid(self, form):

        exam_id = self.kwargs.get('exam_id')
        exam = get_object_or_404(Exam, pk=exam_id)
        form.instance.exam = exam

        return super().form_valid(form)



class QuizListView(ListView,UserPassesTestMixin):
    model = Quiz
    template_name = 'quiz_list.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.are_you_teacher

    def get_queryset(self):
        exam_id = self.kwargs.get('exam_id')
        queryset = Quiz.objects.filter(exam_id=exam_id)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_id'] = self.kwargs.get('exam_id')
        return context



class QuizUpdateView(UpdateView):
    model = Quiz
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_option']
    template_name = 'quiz_update.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.are_you_teacher

    def get_success_url(self):

        exam_id = self.object.exam_id

        return reverse_lazy('quiz_list', kwargs={'exam_id': exam_id})


class QuizSolveView(View):
    def get(self, request, exam_id):

        exam = get_object_or_404(Exam, pk=exam_id)


        quizzes = exam.quizzes.all()

        context = {
            'exam': exam,
            'quizzes': quizzes
        }
        return render(request, 'solve_quiz.html', context)

    def post(self, request, exam_id):
        exam = get_object_or_404(Exam, pk=exam_id)
        quizzes = exam.quizzes.all()

        score = 0
        total = len(quizzes)

        for quiz in quizzes:
            selected_option = request.POST.get(f"answer_{quiz.id}")
            if selected_option == quiz.correct_option:
                score += 1

        if total > 0:
            percent = (score / total) * 100
        else:
            percent = 0

        context = {
            'exam': exam,
            'quizzes': quizzes,
            'score': score,
            'total': total,
            'percent': percent
        }
        return render(request, 'quiz_result.html', context)



