from django import forms
from .models import Blogpost
class Addblog(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields=['post_id','title','head0','chead0','head1','chead1','head2','chead2','author','thumbnail']