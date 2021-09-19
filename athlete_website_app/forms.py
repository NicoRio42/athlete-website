from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email_adress = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}))
    cc_myself = forms.BooleanField(required=False)