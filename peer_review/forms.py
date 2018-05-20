from django import forms
from .models import PeerReview

class PeerReviewForm(forms.ModelForm):

    class Meta:
        model = PeerReview
        fields = ['title', 'feedback', 'score']
