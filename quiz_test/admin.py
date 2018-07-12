from django.contrib import admin
from .models import Profile,Country,City,Category,Test

admin.site.register([Profile,Country,City,Category,Test])
