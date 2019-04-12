from django.db import models
from multiselectfield import MultiSelectField
from django.db.models import Count

class Quiz(models.Model):
    question = models.TextField(max_length=1000,default="")
    option1 = models.TextField(max_length=255,default="")
    option2 = models.TextField(max_length=255, default="")
    option3 = models.TextField(max_length=255, default="")
    option4 = models.TextField(max_length=255, default="")
    explanation = models.TextField(max_length=500, default="")
    answer_choices = (
        (1, 'Option 1'),
        (2, 'Option 2'),
        (3, 'Option 3'),
        (4, 'Option 4'),
    )
    correct_answer = MultiSelectField(choices = answer_choices)

    def __unicode__(self):
        return self.question




