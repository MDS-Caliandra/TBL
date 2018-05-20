from django.conf.urls import url, include
from . import views

app_name = 'peer_review'

peer_review_patterns = [
    url(
        r'^$',
        views.ListPeerReviewView.as_view(),
        name='peer'
    ),
]

urlpatterns = [
    # /profile/<discipline.slug>/groups/...
    url(r'^peer', include(peer_review_patterns)),
]
