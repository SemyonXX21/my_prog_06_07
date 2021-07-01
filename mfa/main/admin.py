from django.contrib import admin
from django.forms import ModelChoiceField


from .models import *
from .models import Lucoshko



admin.site.register(Category)
admin.site.register(Moloko)
admin.site.register(Yaico)
admin.site.register(Ourdt)
admin.site.register(Lucoshko)
