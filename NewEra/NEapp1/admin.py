from unicodedata import category
from django.contrib import admin

# Register your models here.

from .models import contact_info,Category,admin_login, order,product

admin.site.register(contact_info)
admin.site.register(Category)
admin.site.register(admin_login)
admin.site.register(product)
admin.site.register(order)