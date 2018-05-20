from django import forms
from .models import peer_review

class PeerReviewForm(froms.ModelForm):

    class Meta:
        model = peer_review
        fields = ['title', 'feedback', 'score']
