from django.contrib import admin
from .models import Library, Employee, Book, Member, Loan

# Register your models here.
admin.site.register(Library)
admin.site.register(Employee)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Loan)
