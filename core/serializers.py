from rest_framework import serializers
from .models import Book, User, Employee

from django.db import transaction


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "isbn",
            "genre",
            "publisher",
            "year_published",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ["id", "username", "first_name", "last_name"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        models = User
        fields = ["username", "password", "first_name", "last_name"]

    def create(self, validated_data):
        # password = validated_data.pop("password")
        with transaction.atomic():
            user = User.objects.create_user(
                username=validated_data["username"],
                password=validated_data["password"],
                first_name=validated_data.get("first_name", ""),
                last_name=validated_data.get("last_name", ""),
            )
            library = self.context["library"]
            role = self.context.get("role", "librarian")

            Employee.objects.create(user=user, library=library, role=role)
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["user", "library", "role"]
