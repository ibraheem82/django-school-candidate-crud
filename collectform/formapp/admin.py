from re import search
from django.contrib import admin
from .models import Candidate
# Register your models here.

# * inheriting the ModelAdmin in django
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender', 'career']
    
    search_fields = ['name', 'phone', 'email']

    list_fields = ['gender', 'career']
    list_per_page = 10



admin.site.register(Candidate, CandidateAdmin)
    
