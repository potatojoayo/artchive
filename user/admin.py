from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    # admin 사이트의 user에 보여질 속성들
    list_display = (
        'email',
        'name',
        'nickname',
        'date_joined',
        'avatar'
    )

    list_display_links = (
        'email',
        'name',
        'nickname'
    )
