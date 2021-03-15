from django.db import models


# Create your models here.



class Result(models.Model):
    Answer_choice = ((1, '매우아니다'), (2, '아니다'), (3, '보통'), (4, '그렇다'), (5, '매우그렇다'))
    Name=models.CharField(max_length=200,blank=True)
    Question=models.IntegerField(null=False,blank=True,choices=Answer_choice)
    D_result=models.IntegerField(null=True)


