from django.shortcuts import render

from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied

from .serializers import BookSerializer, RegisterSerializer, EmployeeSerializer
from .models import Book, Employee


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(library=user.employee.library)

    def perform_create(self, serializer):
        serializer.save(library=self.request.user.employee.library)


class RegisterView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        employee = self.request.user.employee

        if employee.role != "admin":
            raise PermissionDenied("You don't have permission to create an employee")

        serializer.context["library"] = employee.library
        serializer.save()


class MeView(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.employee
