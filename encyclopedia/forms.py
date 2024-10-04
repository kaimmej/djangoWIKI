



from django import forms

class EntryForm(forms.Form): 

    template_name = "encyclopedia/partials/form_snippet.html"
    name = forms.CharField(
        max_length=100, 
        # label="PostName", 
        # help_text="100 characters max.",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder':'PostName'})
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control post-textarea mb-3', 'placeholder':'PostDescription', 'style': "height: 300px" }), 
        label="Post", 
        )

