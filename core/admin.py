from django.contrib import admin
from .models import Article, Employee

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name','address','price','category')
    ordering = ('name',)
    
class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('rut','lastname','name','dob','email')
    ordering = ('lastname','name','rut')
    
admin.site.register(Article,ArticleAdmin)
admin.site.register(Employee,EmployeeAdmin)
