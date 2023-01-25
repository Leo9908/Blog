from django.contrib import admin
from .models import (Post, Comment, PostView, Like, User)

# Register your models here.
# Aqui se registran los modelos solo para poderlos editar en
# la vista de admin
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(User)
