from django.contrib.auth import get_user_model
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView
)

# App imports
from disciplines.models import Discipline
from .models import PeerReview
from .forms import PeerReviewForm

User = get_user_model()

class ListPeerReviewView(ListView):

    template_name = 'peer_review/peer.html'
    context_object_name = 'peer_review'

    def get_discipline(self):

        discipline = Discipline.objects.get(
            slug=self.kwargs.get('slug', '')
        )

    def get_context_data(self, **kwargs):

        context = super(ListPeerReviewView, self).get_context_data(**kwargs)
        context['discipline'] = self.get_discipline()
        context['form'] = PeerReviewForm()
        return context

    def get_queryset(self):

        discipline = self.get_discipline()
        peer_review = PeerReview.objects.filter(discipline=discipline)
        return peer_review
