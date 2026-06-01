from django.contrib import admin
from .models import Test_session, Guruh, Kurs, Savol

admin.site.register(Savol)

admin.site.register(Kurs)
admin.site.register(Guruh)
admin.site.register(Test_session)
