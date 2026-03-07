from django.core.management.base import BaseCommand
from school.models import Student, Teacher


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **kwargs):
        teachers = Teacher.objects.all()
        students = Student.objects.all()

        # print(teachers, students)        
        for s in students:
            for t in teachers:
                s.teachers.add(t)
        
        s = students.get(id=1)
        ts = s.teachers.all()
        print(ts)