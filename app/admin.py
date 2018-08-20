from django.contrib import admin

# Register your models here.
from app.models import User, Product, Exchange

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Exchange)