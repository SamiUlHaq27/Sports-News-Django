from django.forms import ModelForm
from DB.models import Blog, Comment
import django_filters

class MyForm(ModelForm):
    class Meta():
        model = Comment
        fields = ["profile_picture","text","name","email","website"]

class MyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    class meta():
        model = Blog
        fields = ['our_category','title']