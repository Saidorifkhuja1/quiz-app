from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTeacherPageView.as_view(), name='home'),
    path('exam_create/', ExamCreateView.as_view(), name='exam_create'),
    path('exam_list/', ExanListView.as_view(), name='exam_list'),
    path('exam_detail/<int:pk>/', ExamDetailView.as_view(), name='exam_detail'),
    path('quiz/create/<int:exam_id>/', QuizCreateView.as_view(), name='quiz_create'),
    path('exam/<int:exam_id>/quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz_update'),
    path('quiz/solve/<int:exam_id>/', QuizSolveView.as_view(), name='quiz_solve'),

]