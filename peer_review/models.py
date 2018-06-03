from django.utils.translation import ugettext_lazy as _
from django.db import models


class PeerReview(models.Model):

    session = models.PositiveSmallIntegerField(
        _('Session'),
        default=0,
    )

    username_received = models.CharField(
        _('User'),
        max_length=30,
    )

    username_gave = models.CharField(
        _('User'),
        max_length=30,
    )

    feedback = models.TextField(
        _('Feedback'),
        help_text=_('Feedback about your teammate ')
    )

    score = models.PositiveSmallIntegerField(
        _('Score'),
        blank=True,
        help_text=_("Score your teammate")
    )


    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent
        the object.
        """

        return '{0}: {1} - {2}'.format(self.username_received, self. feedback, self.score)

    class Meta:
        verbose_name = _('PeerReview')
        verbose_name_plural = _('PeerReviews')
        ordering = ['username_received', 'username_gave']

class PeerReviewFormModel(models.Model):

    feedback = models.TextField(
        _('Feedback'),
        help_text=_('Feedback about your teammate ')
    )

    score = models.PositiveSmallIntegerField(
        _('Score'),
        blank=True,
        help_text=_("Score your teammate")
    )
