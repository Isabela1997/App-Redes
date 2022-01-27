### Código adaptado da playlist do canal Codemy: https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi ###
from django import forms
from .models import Post, Category

#cats = [("Educação", "Educação"), ("Esportes", "Esportes")]
cats = Category.objects.all().values_list("name", "name")

choice_list = []

for item in cats:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "category", "body", "header_image", "snippet")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Coloque aqui o título da sua Publicação"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control", "placeholder": "Coloque aqui o título da Web Page"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(choices=choice_list, attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escreva aqui sua Publicação"}),
            "snippet": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escreva aqui o resumo de sua Publicação"}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body", "header_image", "snippet")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Coloque aqui o título do seu post"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control", "placeholder": "Coloque aqui o título da web page"}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escreva aqui sua publicação"}),
            "snippet": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escreva aqui sua publicação"}),
        }