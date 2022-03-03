from django.contrib import admin
from.models import contact_info,products,category,restframework,order

# Register your models here.
admin.site.register(contact_info)
admin.site.register(products)
admin.site.register(category)
admin.site.register(order)
admin.site.register(restframework)