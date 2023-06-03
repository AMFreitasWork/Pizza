from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label="Topping 1", max_length=10)
#     topping2 = forms.CharField(label="Topping 2", max_length=10)
#     topping3 = forms.CharField(label="Topping 3", max_length=10)
#     topping4 = forms.CharField(label="Topping 4", max_length=10)
#     size = forms.ChoiceField(label="Size", choices=[('Pequena', 'Pequena'), ('Media', 'Media'), ('Grande', 'Grande'), ('Familiar', 'Familiar')])

class PizzaForm(forms.ModelForm):
    
    
    class Meta:
        model = Pizza 
        fields = ['topping1','topping2','topping3','topping4', 'size']
        labels= {'topping1':'Topping 1','topping2':'Topping 2','topping3':'Topping 3','topping4':'Topping 4'}

class MultiplePizzaForm(forms.Form):
    number= forms.IntegerField(min_value=2, max_value=6)
        


