from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'superman@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
        ]
        marvel_users = [User.objects.create(username=u['username'], email=u['email'], first_name=u['first_name'], last_name=u['last_name'], password=make_password('password')) for u in marvel_heroes]
        dc_users = [User.objects.create(username=u['username'], email=u['email'], first_name=u['first_name'], last_name=u['last_name'], password=make_password('password')) for u in dc_heroes]

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel_team = Team.objects.create(name='Team Marvel')
        marvel_team.members = marvel_users
        marvel_team.save()
        dc_team = Team.objects.create(name='Team DC')
        dc_team.members = dc_users
        dc_team.save()

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        for user in marvel_users + dc_users:
            Activity.objects.create(user=user, type='Running', duration=30, calories=300)
            Activity.objects.create(user=user, type='Cycling', duration=45, calories=400)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        for user in marvel_users + dc_users:
            Workout.objects.create(user=user, suggestion='Pushups, Situps, Squats')

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel_team, score=1200)
        Leaderboard.objects.create(team=dc_team, score=1100)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
