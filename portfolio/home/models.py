from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    profile = models.ImageField(upload_to='profile/')
    desc = models.TextField()
    email = models.EmailField(max_length=254)
    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.name +'---'+ self.email
    

class Projects(models.Model):
    pname = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='projects/')
    pdesc = models.TextField()
    link = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.pname

    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name +"---"+ self.email
   