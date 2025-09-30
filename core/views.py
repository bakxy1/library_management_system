from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import BookSerializer
from .models import Book


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(library=user.employee.library)

    def perform_create(self, serializer):
        serializer.save(library=self.request.user.employee.library)
