from django import forms
from .models import Article, Employee


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        
        fields = ('name','address','price','category')
        
        labels = {
            'name':'Nombre',
            'address':'Dirección',
            'price':'Precio',
            'category':'Categoría'
        }
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'address':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'price':forms.TextInput(attrs={'class':'form-control mb-3','type':'number'}),
            'category':forms.TextInput(attrs={'class':'form-control mb-3'})            
        }


class EmployeeForm(forms.ModelForm):

    class Meta:
        model =  Employee

        fields = ('rut','name','lastname','dob', 'email')

        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'name':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'lastname':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'dob':forms.DateInput(attrs={'class':'form-control mb-3','type':'date'}),
            'email':forms.EmailInput(attrs={'class':'form-control mb-3','type':'email'})
        }
