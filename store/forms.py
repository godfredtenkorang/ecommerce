from django import forms
from .models import Review, Comment, ReviewComment


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))
    
    class Meta:
        model = Review
        fields = ['comment', 'rate']
        
class ReplyForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholdet': 'Reply here ...',
        'row': '4',
    }))
    
    class Meta:
        model = ReviewComment
        fields = ['comment']
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))
    
    class Meta:
        model = Comment
        fields = ('content',)