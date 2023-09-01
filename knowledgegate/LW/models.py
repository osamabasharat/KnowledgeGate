from django.db import models
from tinymce import models as tinymce_models




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
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100, blank=True)
    content = tinymce_models.HTMLField() 
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    image = models.ImageField(upload_to='topic_images/', default=None, null=True)
    points = tinymce_models.HTMLField() 
 

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = tinymce_models.HTMLField()
    answer = tinymce_models.HTMLField()

    def __str__(self):
        return self.question
    
class About(models.Model):
    content = tinymce_models.HTMLField() 
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    right_text = tinymce_models.HTMLField() 
    # video = models.FileField(upload_to='about_videos/', blank=True, null=True)

    def __str__(self):
        return "About Us"