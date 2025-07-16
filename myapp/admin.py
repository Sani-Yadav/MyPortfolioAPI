from django.contrib import admin
from .models import *  # Import all models from your app


admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact)

