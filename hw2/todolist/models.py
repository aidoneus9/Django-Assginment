from django.db import models
# DB
# Model = DB의 테이블
# Field = DB의 컬럼

# fields: title, description, start_date, end_date, is_completed, created_at, modified_at
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # admin
    class Meta:
        verbose_name = '할일쿵야'
        verbose_name_plural = '주먹밥쿵야의 할 일 떠안기'

# class TodoCategory(models.Model):