from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
#
# from quiz.account.models import Customer


class Exam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    time_limit_minutes = models.PositiveIntegerField(null=True, blank=True, help_text='Vaqt limiti minutlarda bo\'lishi kerak ')

    def __str__(self):
        return self.title


class Quiz(models.Model):
    exam = models.ForeignKey(Exam, related_name='quizzes', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100, help_text="To\'g\'ri javob ,bu yerga to\'ti javob tozilgan variant tartib raqamini yozing  ( masalan ,1 yoki 2 yoki 3 .)")

    def __str__(self):
        return f"{self.exam.title} - {self.question}"

    def save(self, *args, **kwargs):
        # Check the number of existing quizzes related to this exam
        if self.exam.quizzes.count() >= 100:
            raise ValueError("Bitta imtixonda eng ko\'pi  100 ta savol bo\'lishi mumkin  ")

        super().save(*args, **kwargs)

# class QuizResult(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     score = models.IntegerField()
#
#     def __str__(self):
#         return f"{self.user.username} - {self.quiz.question} - Score: {self.score}"












