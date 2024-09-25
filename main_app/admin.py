from django.contrib import admin
# import your models here
from .models import Goal, Step, Milestone

# Register your models here
admin.site.register(Goal)
admin.site.register(Step)
admin.site.register(Milestone)