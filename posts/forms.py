from django import forms

class PostCreatForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=2, max_length=254)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()



class ReviewCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)



