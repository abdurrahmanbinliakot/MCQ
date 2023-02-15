from django.db import models

from ckeditor.fields import RichTextField

class Articless(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True, default="Empty Title")
    content = RichTextField()
    def __str__(self):
        return self.title or None

# Create your models here.
STATUS = (
        ('H', 'Hard'),
        ('M', 'medium'),
        ('E', 'easy'),
    )

ANS_OPS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

class Class(models.Model):

    class_name=models.CharField(max_length=100)
    # subject_name=models.ForeignKey(Subject,models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.class_name
class Subject(models.Model):

    subject_name=models.CharField(max_length=100)
    class_name=models.ForeignKey(Class,models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.subject_name
class Chapter(models.Model):

    chapter_name=models.CharField(max_length=100,blank=True,null=True)
    subject_name=models.ForeignKey(Subject,models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.chapter_name

class MCQ(models.Model):

    # class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter_field = models.ForeignKey(Chapter, on_delete=models.CASCADE,blank=True,null=True)
    question_text = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    options_A = models.CharField(max_length=100)
    options_B = models.CharField(max_length=100)
    options_C = models.CharField(max_length=100)
    options_D = models.CharField(max_length=100)
    # answer = models.CharField(max_length=100)
    answer = models.CharField(max_length=10, choices=ANS_OPS)
    status = models.CharField(max_length=10, choices=STATUS)
    is_multiple_select = models .BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        
        return self.question_text
    

