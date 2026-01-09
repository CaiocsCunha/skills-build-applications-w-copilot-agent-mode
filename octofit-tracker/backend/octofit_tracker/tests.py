from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activeuser')
        activity = Activity.objects.create(user=user, type='run', duration=30, calories=300)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Leaderboard Team')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='workoutuser')
        workout = Workout.objects.create(user=user, suggestion='Pushups')
        self.assertEqual(workout.suggestion, 'Pushups')
