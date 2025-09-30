from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=[("admin", "Admin"), ("librarian", "Librarian")],
        default="librarian",
    )

    def __str__(self) -> str:
        return f"{self.user.username} @ {self.library.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    publisher = models.CharField(max_length=100)
    year_published = models.IntegerField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="books")

    class Meta:
        unique_together = ("isbn", "library")

    def __str__(self) -> str:
        return f"{self.title} by {self.author} in library: {self.library.name}"


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_id = models.CharField(max_length=20, unique=True)
    library = models.ForeignKey(
        Library, on_delete=models.CASCADE, related_name="members"
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.membership_id}) @ {self.library.name}"


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("book", "member", "loan_date")

    def __str__(self) -> str:
        return f"{self.book.title} loaned to {self.member.name} on {self.loan_date}"
