from django import forms
from app.models import *
from django.utils.translation import gettext_lazy as _
# for creating model forms we have inherit each and every class with ModelForm class of froms module
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'



class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['name']
        #widgets={'columnnanme1':value1,'column2':value2,........}
        widgets={'name':forms.Textarea(attrs={'cols':5,'rows':5})}
        labels={'name':_('Ur name'),'url':_('ur url')}
        help_texts={'name':_('enter ur name ')}





class AccessForm(forms.ModelForm):
    class Meta:
        model=Access_Records
        fields='__all__'



