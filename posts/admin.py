#Posts model

#Django
from django.contrib import admin
from posts.models import Post


@admin.register(Post)


class postAdmin(admin.ModelAdmin):
    #Post admin

    list_display = ('id','user','title','created','photo')
    list_filter =['created','modified',]

    search_fields = ['title', 'user__username', 'user__email',]