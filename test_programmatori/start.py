#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_programmatori.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(['manage.py', 'makemigrations', 'form'])
    execute_from_command_line(['start.py', 'migrate'])

    from django.contrib.auth.models import User
    # SuperUser creation:
    admin = User.objects.create_superuser('admin', 'admin@admin.it', 'admin')
    print('MIGRATION AND SUPERUSER CREATION DONE!\nSUPERUSER CREDENTIALS:\nUsername: admin\nPassword: admin')
    from form.models import Job
    # Job Example Class creation:
    job1 = Job.objects.create(role="Cuoco",
                             duty="Cuoco primi",
                             location='Milano',
                             description='Per la sede di Milano si cerca un cuoco specializzato nei primi piatti della cucina milanese con almeno 5 anni di esperienza'
                             )
    job2 = Job.objects.create(role="Cuoco",
                             duty="Cuoco secondi",
                             location='Milano',
                             description='Per la sede di Milano si cerca un cuoco specializzato nei secondi piatti della cucina milanese con almeno 2 anni di esperienza'
                             )
    job3 = Job.objects.create(role="Cuoco",
                              duty="Cuoco primi",
                              location='Roma',
                              description='Per la sede di Roma, si cerca cuoco specializzato nei primi piatti della cucina romana, con almeno 2 anni di esperienza'
                              )
    job4 = Job.objects.create(role="Cameriere",
                              duty="Cameriere di sala",
                              location='Genova',
                              description='Per la sede di Genova, si cerca cameriere di sala con almeno 2 anni di esperienza.'
                              )
    job5 = Job.objects.create(role="Cameriere",
                              duty="Cameriere di sala",
                              location='Milano',
                              description='Per la sede di Milano si cerca cameriere di sala con almeno 2 anni di esperienza.'
                              )
    job6 = Job.objects.create(role="Cameriere",
                              duty="Maitre",
                              location='Milano',
                              description='Per la sede di Milano si cerca Maitre con decennale esperienza.'
                              )

if __name__ == '__main__':
    main()
