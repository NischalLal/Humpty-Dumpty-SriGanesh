from django.contrib import admin
from .models import Post, Project, SocialSite, Contact, About

# Register your models here

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(SocialSite)
admin.site.register(Contact)
admin.site.register(About)