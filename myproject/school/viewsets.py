from django.contrib.auth.models import User
from rest_framework import viewsets
from school.serializers import UserSerializer,TeacherSerializer
from school.models import Teacher


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset= Teacher.objects.all()
    serializer_class = TeacherSerializer