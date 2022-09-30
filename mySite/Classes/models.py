from django.db import models

# Create your models here.

class StudentClass(models.Model):
    class_name = models.CharField('Class name',max_length=200)
    def __str__(self):
        return self.class_name
    
class Student(models.Model):
    student_id = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    student_fam = models.CharField('Last Name',max_length=200)
    student_im = models.CharField('First Name',max_length=200)
    student_otch = models.CharField('Second name',max_length=200)
    student_birthd = models.DateField('birth date')
    def __str__(self):
        return self.student_fam + " " + self.student_im + " " + self.student_otch
