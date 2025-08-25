from django.contrib import admin
from .models import Question, Choice

# บอก Django ให้โชว์ Question กับ Choice บนหน้า Admin
admin.site.register(Question)
admin.site.register(Choice)