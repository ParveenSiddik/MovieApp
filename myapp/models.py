from django.db import models

class GenreChoices(models.TextChoices):
    THRILLER='Thriller','Thriller'
    ACTION='Action','Action'
    SCI_FI="Scifi",'Scifi'

# GENRE_CHOICES=[('Thriller','Thriller'),
#                ('Action','Action'),
# ]


class Movies(models.Model):
        

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200,choices=GenreChoices.choices)
    # genre=models.CharField(max_length=200,choices=GENRE_CHOICES)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)


# class ClassChoices(models.IntegerChoices):
#     ONE=(1,1)
#     TWO=(2,2)
#     THREE=(3,3)
#     FOUR=(4,4)
#     FIVE=(5,5)
#     SIX=(6,6)
#     SEVEN=(7,7)
#     EIGHT=(8,8)
#     NINE=(9,9)
#     TEN=(10,10)

# class DivisionChoices(models.TextChoices):

#     A=('A','A')
#     B=('B','B')
#     C=('C','C')
#     D=('D','D')    

# class Student(models.Model):
#     name=models.CharField(max_length=200)

#     classes=models.CharField(max_length=200,choices=ClassChoices.choices)

#     division=models.CharField(max_length=200,choices=DivisionChoices.choices)

#     contact=models.CharField(max_length=200)

#     about_me=models.TextField()

#     photo=models.ImageField()

#     webaddress=models.URLField


# class Car(models.Model):
#     name=models.CharField(max_length=200)

#     model=models.CharField(max_length=200)

#     seat_capacity=models.IntegerField()

#     fuel_type=models.CharField(max_length=200,choices=FuelClass.Choices)

#     release_date=models.DateField

#     Stock=models.BooleanField(max_length=200,choices=StockClass.choices)

#     Year=models.DateField()

#     perfomance=models.FloatField()

# class Customer(models.Model):
#     first_name=models.CharField(max_length=200)
#     last_name=models.CharField(max_length=200)    




       

