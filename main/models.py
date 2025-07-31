from django.db import models
# Create your models here.
class Profile(models.Model):  
    profile_image = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class SocialMedia(models.Model):
    url = models.URLField()                     
    icon_class = models.CharField(max_length=100)  # e.g. fab fa-twitter

    def __str__(self):
        return self.icon_class

class Buttons(models.Model):
    button_name = models.CharField(max_length=40)                 
    cv_url = models.URLField()         
    contact_button_name = models.CharField(max_length=40)                 
    mobile_url = models.URLField()  #For URL 
    def __str__(self):
        return self.button_name
    
class AboutMe(models.Model):
    title_name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.title_name
class PersonalDetails(models.Model):
    icon_class = models.CharField(max_length=50)  # for icon class
    label = models.CharField(max_length=40)  
    value = models.CharField(max_length=50) 
    def __str__(self):
        return self.label
class Skills(models.Model):
    name = models.CharField(max_length=50)
    icon_image = models.ImageField(upload_to='skills/')
    def __str__(self):
        return self.name


class Expericence(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    responsibilities = models.TextField()
    def __str__(self):
        return self.position

class Education(models.Model):
    degree_title = models.CharField(max_length=100)  
    university_name = models.CharField(max_length=150) 
    start_year = models.IntegerField() 
    end_year = models.IntegerField()    
    duration = models.CharField(max_length=50)  
    location = models.CharField(max_length=100)  
    def __str__(self):
        return self.degree_title

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    

class Project(models.Model):
    title = models.CharField(max_length=100)  
    description = models.TextField()  
    # technologies = models.CharField(max_length=200) 
    technologies = models.ManyToManyField(Technology) 
    image = models.ImageField(upload_to='projects/') 
    git_url = models.URLField() 
    live_demo_url = models.URLField()                     


    def __str__(self):
        return self.title









