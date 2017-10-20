from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):

    question_text = models.CharField("讲师", max_length=200)
    pub_date = models.DateTimeField("分享时间")

    def was_published_recently(self):

        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        
        return self.question_text
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最新发布?'
class Choice(models.Model):

    question = models.ForeignKey(Question)
    choice_text = models.CharField("主题", max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):

        return self.choice_text
    
