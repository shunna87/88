from django import forms 
from .models import Post, Category


#choices = [('China', 'China'), ('Chengyu', 'Chengyu'), ('Films', 'Films'),]
choices = Category.objects.all().values_list('name','name')

choice_list =[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image',  'snipped', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'author': forms.TextInput(attrs= {'class': 'form-control', 'value': '', 'id':'elder', 'type': 'hidden'}),
            'category': forms.Select(choices = choice_list, attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            'snipped': forms.TextInput(attrs= {'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image',  'snipped','category', 'body')

        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            'snipped': forms.TextInput(attrs= {'class': 'form-control'}),
            
        }        