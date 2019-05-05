from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    profile_image = models.ImageField(blank=True, null=True,upload_to="images/students/")
    def __str__(self):
        return self.first_name + self.last_name

class Level(models.Model):
    LEVEL = [
        ("N","Nursery"),
        ("KG","Kindergarden"),
        ("ONE","One"),
        ("TWO","Two"),
        ("THREE","Three"),
        ("FOUR","Four"),
        ("FIVE","Five"),
        ("SIX","Six"),
        ("SEVEN","Seven"),
        ("EIGHT","Eight"),
        ("NINE","Nine"),
        ("TEN","Ten"),
        ("ELEVEN","Eleven"),
        ("TWELVE","Twelve")
    ]
    level = models.CharField(max_length=30, choices= LEVEL)

    def __str__(self):
        return self.level


class Subject(models.Model):
    name = models.CharField(max_length=30)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '-' + self.level.level

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    subject = models.ManyToManyField(Subject)
    level = models.ManyToManyField(Level)
    profile_image = models.ImageField(blank=True, null=True,upload_to="images/teachers/")

    def __str__(self):
        return self.first_name + self.last_name


    
