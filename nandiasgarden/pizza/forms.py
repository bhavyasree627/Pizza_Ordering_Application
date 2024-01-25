from django import forms
from .models import Pizza

class  PizzaForm(forms.ModelForm):
    # image=forms.ImageField()
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2','size']
        labels={'topping1':'Topping 1','topping2': 'Topping 2'} 

class MultiplePizzaForm(forms.Form):
    number=forms.IntegerField(min_value=2,max_value=6)
    