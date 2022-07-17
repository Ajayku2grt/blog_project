from django import forms
from blog.models import Post,Comment   #call particular function from model

class PostForm(forms.ModelForm):

    class Meta():
        model = Post     #connect model which using
        fields = ('author', 'title', 'text')  #add field name which to be use in form


        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }



class CommentForm(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
