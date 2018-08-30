import os
import json
import datetime
import django
import subprocess
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aboutme.settings")
django.setup()
from django.contrib.auth.models import User
from main_app.models import *


def run_process(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    while process.poll() is None:
        print(process.stdout.readline())
    process.wait()
    return process.returncode


def fill_db(data):
    p = Person()
    p.name = data['name']
    p.surname = data['surname']
    p.birthday = data['birthday']
    p.save()
    work = Work()
    work.organization = "Test org"
    work.site = "http://www.test.ru"
    work.official_duties = "Test test test"
    work.position = "test position"
    work.region = "test_region"
    work.start_time = datetime.datetime(year=2000, month=1, day=1)
    work.save()


def create_super_user():
    with open(os.path.join('json', 'super.json'), 'r', encoding='utf-8') as super_file:
        sd = json.load(super_file)
        super = User.objects.create_superuser(sd['name'], sd['email'], sd['pwd'])
        super.save()

if __name__ == '__main__':
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3')
    if os.path.exists(db_path):
        os.remove(db_path)
        run_process('python3 manage.py makemigrations')
        run_process('python3 manage.py migrate')

    with open(os.path.join('json', 'person.json'), 'r', encoding='utf-8') as f:
        fill_db(json.load(f))

    create_super_user()