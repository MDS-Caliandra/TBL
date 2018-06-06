from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from peer_review.models import PeerReview
from disciplines.models import Discipline
from TBLSessions.models import TBLSession
from model_mommy import mommy
from core.test_utils import user_factory

User = get_user_model()


class PeerReviewTestModel(TestCase):

    def setUp(self):
        """
        This method will run before any test case.
        """
        self.client = Client()
        self.peer_review = PeerReview()
        self.teacher = User.objects.create_user(
            username='Test1',
            email='test1@gmail.com',
            password='teacher1'
        )

        self.student = User.objects.create_user(
            username='Test3',
            email='test3@gmail.com',
            password='student1',
            is_teacher=False
        )
        self.discipline = mommy.make(
            Discipline,
            teacher=self.teacher,
            title='Discipline',
            course='Engineering',
            password='discipline1',
            students_limit=5,
            students=[self.student],
            make_m2m=True
        )

        self.session = mommy.make(
            TBLSession,
            discipline=self.discipline,
            title='Test Session',
            description='Session for test',
            make_m2m=True
        )

        self.peer_review = mommy.make(
            PeerReview,
            feedback='Feedback test',
            score=10
        )


        self.client.login(
            username=self.teacher.username, password='teacher1'
        )

    def tearDown(self):
        """
        This method will run after any test.
        """

        self.teacher.delete()
        self.student.delete()
        self.session.delete()
        self.peer_review.delete()

    def teste_feedback(self):


        self.client.logout()
        self.client.login(
            username=self.student.username, password='student1'
        )

        self.assertEqual(self.peer_review.feedback, 'Feedback test')


    def test_score(self):


        self.client.logout()
        self.client.login(
            username=self.student.username, password='student1'
        )

        self.assertEqual(self.peer_review.score, 10)
