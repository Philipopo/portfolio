from django.contrib import admin
from .models import Project, Category, Certificate, Contact, Reviews

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
 
    list_display = ('name',  'category', 'date')
    search_fields = ('name', 'description', 'category',)

    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Certificate)
admin.site.register(Contact)
admin.site.register(Reviews)