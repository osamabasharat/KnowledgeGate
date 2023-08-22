from django.db import models
class Classes(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Subject(models.Model):
    name = models.CharField(max_length=50)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    content = models.TextField() #text content of topic
    image = models.ImageField(upload_to='topic_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
# from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)