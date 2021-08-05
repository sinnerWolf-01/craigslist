from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    #this gives us a way to name plurals of our class models 
    def __str__(self):
        return '{}'.format(self.search)
    class Meta:
        verbose_name="Search"
        verbose_name_plural = 'Searches'
        



