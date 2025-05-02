from django.db import models

class Todo(models.Model):
    CATEGORY_CHOICES = (
        ('programming', '코딩'),
        ('workout', '운동'),
        ('chores', '집안일'),
        ('appointment', '약속'),
        ('others', '기타')
    )

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # admin 페이지
    def __str__(self):
        return f'[{self.category}] {self.title}'

    class Meta:
        verbose_name = '할일쿵야'
        verbose_name_plural = '주먹밥쿵야의 할 일 떠안기'

