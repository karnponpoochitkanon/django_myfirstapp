import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

def create_question(text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date=time)

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        q = create_question("future", days=+30)
        self.assertIs(q.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        q = create_question("old", days=-2)
        self.assertIs(q.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        q = create_question("recent", days=-1)
        self.assertIs(q.was_published_recently(), True)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, "No polls are available.")

    def test_past_question_shown(self):
        create_question("past", days=-1)
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, "past")

    def test_future_question_not_shown(self):
        create_question("future", days=+1)
        resp = self.client.get(reverse("index"))
        self.assertNotContains(resp, "future")