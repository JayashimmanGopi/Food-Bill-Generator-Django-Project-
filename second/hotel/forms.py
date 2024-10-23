from django.forms import ModelForm, models
from hotel.models import item

class Itemform(ModelForm):
    class Meta:
        model=item
        fields={"dish","cost"}  #'__all__'