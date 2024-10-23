from django.db import models
from django.urls import reverse

# Create your models here.
class item(models.Model):
    dish=models.CharField(max_length=400)
    cost=models.IntegerField(max_length=27)
    
    def __str__(self):
        return f" Dish = {self.dish} : Cost = {self.cost}"
    
    def get_detail_url(self):
        return reverse("detailpage",args=[self.id])
    
    def get_update_url(self):
        return reverse("updateview",args=[self.id])
    
    def get_delete_url(self):
        return reverse("deleteview",args=[self.id])
    
    def get_home_url(self):
        return reverse("homepage")
    
    
