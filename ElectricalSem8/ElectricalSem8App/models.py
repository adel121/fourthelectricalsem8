from django.db import models

# Create your models here.


Discipline_Choices = ( ('power','POWER'), ('telecom','TELECOM'), ('common','COMMON'))

class Course(models.Model):
	def __str__(self):
		return self.Name
	Name = models.CharField(max_length=100, primary_key="True")
	Discipline = models.CharField(max_length=100, choices=Discipline_Choices,default="telecom")

class Video(models.Model):
	def __str__(self):
		return str(self.Course) + " " + str(self.Lecture_Number)
	Youtube = models.CharField(max_length=300, default="https://youtube.com")
	Drive = models.CharField(max_length=300,null=True, blank=False)
	Date = models.DateTimeField('Date In', blank=False, null=True)
	Lecture_Number = models.FloatField(null=True, blank=False)
	Course = models.ForeignKey(Course, on_delete=models.CASCADE, default="Microprocessor II")

class Document(models.Model):
	def __str__(self):
		return str(self.Course) + "/" +self.Name
	Name = models.CharField(max_length=100, primary_key="True")
	Format = models.CharField(max_length=100,)
	Notes = models.CharField(max_length=100,)
	Drive = models.CharField(max_length=300,null=True, blank=False)
	Course = models.ForeignKey(Course, on_delete=models.CASCADE, default="Microprocessor II")
	