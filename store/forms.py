from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))
    
    class Meta:
        model = Review
        fields = ['comment', 'rate']