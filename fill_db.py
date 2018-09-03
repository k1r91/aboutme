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


def fill_person():
    Person.objects.all().delete()
    with open(os.path.join('json', 'person.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
        p = Person()
        p.name = data['name']
        p.surname = data['surname']
        p.birthday = data['birthday']
        p.about_desc = ''.join(data['about_desc'])
        p.location = data['location']
        p.email = data['email']
        p.phone = data['phone']
        p.save()


def fill_works():
    Work.objects.all().delete()
    with open(os.path.join('json', 'works.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
        for work in data['works']:
            tswork = Work()
            tswork.organization = work['organization']
            tswork.region = work['region']
            tswork.site = work['site']
            tswork.position = work['position']
            tswork.official_duties = ''.join(work['official_duties'])
            tswork.start_time = work['start_time']
            try:
                tswork.end_time = work['end_time']
            except KeyError:
                pass
            tswork.save()


def fill_education():
    Education.objects.all().delete()
    with open(os.path.join('json', 'education.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
        for edu in data['education']:
            tsedu = Education()
            tsedu.site = edu['site']
            tsedu.name = edu['name']
            tsedu.description = "".join(edu['description'])
            tsedu.end_date = edu['end_date']
            tsedu.location = edu['location']
            tsedu.speciality = edu['speciality']
            tsedu.save()


def create_super_user():
    with open(os.path.join('json', 'super.json'), 'r', encoding='utf-8') as super_file:
        sd = json.load(super_file)
        super = User.objects.create_superuser(sd['name'], sd['email'], sd['pwd'])
        super.save()


if __name__ == '__main__':
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3')
    # if os.path.exists(db_path):
    #     os.remove(db_path)
    #     run_process('python3 manage.py makemigrations')
    #     run_process('python3 manage.py migrate')

    fill_person()
    fill_works()
    fill_education()

    # create_super_user()