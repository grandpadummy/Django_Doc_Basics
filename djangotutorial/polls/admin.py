from django.contrib import admin
from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)

admin.site.site_header = "Quiz App"
admin.site.site_title = "Quiz App?"
admin.site.index_title = "Do You Know?"