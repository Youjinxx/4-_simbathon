from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "question/", blank=True, null=True)
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]

class Answer(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.content