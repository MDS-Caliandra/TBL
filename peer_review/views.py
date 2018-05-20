from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, DetailView
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

class CreatePeerReviewView(CreateView):

    model = PeerReview
    template_name = ""
    form_class = PeerReviewForm

    def get_discipline(self):

        discipline = Discipline.objects.get(
            slug=self.kwargs.get('slug', '')
        )

        return discipline

    def get_success_url(self):

        discipline = self.get_discipline()

        success_url = reverse_lazy(
            'PeerReview:list',
            kwargs={'slug': discipline.slug}
        )

        return success_url

class EditPeerReviewView(UpdateView):

    model = PeerReview
    template_name = 'peer_review/form.html'
    context_object_name = 'peer_review'
    form_class = PeerReviewForm

    def get_discipline(self):

        discipline = Discipline.objects.get(
            slug=self.kwargs.get('slug', '')
        )

        return discipline

    def get_context_data(self, **kwargs):

        context = super(EditPeerReviewView, self).get_context_data(**kwargs)
        context['discipline'] = self.get_discipline()
        return context

    def get_success_url(self):

        discipline = self.get_discipline()

        success_url = reverse_lazy(
            'PeerReview:list',
            kwargs={'slug': discipline.slug}
        )

        return success_url

class ShowPeerReviewView(DetailView):

    template_name = 'peer_review/#'
    context_object_name = 'peer_review'

    def get_discipline(self):

        discipline = Discipline.objects.get(
            slug=self.kwargs.get('slug', '')
        )

        return discipline


    def get_object(self):

        discipline = self.get_discipline()

        peer_review = PeerReview.objects.get(
            Q(discipline=discipline),
            Q(pk=self.kwargs.get('pk', ''))
        )

        return peer_review

    def get_context_data(self, **kwargs):


        peer = self.get_object()
        peer_review = get_datetimes(peer)

        context = super(ShowPeerReviewView, self).get_context_data(**kwargs)
        context['discipline'] = self.get_discipline()
        return context
