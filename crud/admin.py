from django.contrib import admin

# Register your models here.
from . models import BookList
admin.site.register(BookList)



from . models import Productlist
admin.site.register(Productlist)
