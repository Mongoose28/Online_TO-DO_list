from django.db import models

class Registration(models.Model):
    first_name=models.CharField(max_lentgth=250)
    Last_name=models.CharField(max_length=250)
    Phone=models.CharField(max_length=11)
    Email=models.CharField(max_length=250)
    Password=models.CharField(max_length=50)




class User(models.Model):
    user=models.CharField(max_length=250)
    password=models.CharField(max_length=200)


class Task(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    Project_name=models.CharField(max_length=300)
    Status=models.CharField(max_length=10)

class reminder(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Date=models.CharField(max_length=120)
    time=models.CharField(max_length=100)



