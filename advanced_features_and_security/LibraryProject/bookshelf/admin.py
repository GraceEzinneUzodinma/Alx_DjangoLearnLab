from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
class  CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser')
    fieldsets =(
        (None,{'fields':('date_of_birth', 'profile_photo')}),
        ('permissions', {'fields':('is_staff', 'is_superuser')})
    )
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
