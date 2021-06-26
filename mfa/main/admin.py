from django.contrib import admin
from django.forms import ModelChoiceField


from .models import *



admin.site.register(Category)
admin.site.register(Moloko) #, MolokoAdmin)
admin.site.register(Yaico)#, YaicoAdmin)
admin.site.register(Ourdt)
#admin.site.register(Cart)
#admin.site.register(Customer)