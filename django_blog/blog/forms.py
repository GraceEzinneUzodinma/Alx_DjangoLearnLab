from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        max_length=500,  # validation: max 500 characters
        required=True,
        help_text="Maximum 500 characters."
    )

    class Meta:
        model = Comment
        fields = ['content']

    # Optional: custom validation
    def clean_content(self):
        data = self.cleaned_data['content']
        if "badword" in data.lower():  # example: prevent bad words
            raise forms.ValidationError("Please avoid using inappropriate language.")
        return data
