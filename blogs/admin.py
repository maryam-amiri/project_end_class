from django.contrib import admin
from . import  models
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','price','is_active','description']
    list_editable = ['price','is_active']
    # readonly_fields = ['slug']
    prepopulated_fields = {'slug':['title']}
    list_filter = ['is_active','price']

#baraye sazman dehie dastebandi ha dar admin class tarif mikonim:

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']
    list_editable = ['url_title']

class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['color', 'size']
    list_editable = ['size']

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['tag']


#bayad dar payin tarif konim class ra:

admin.site.register(models.Product,ProductAdmin)

#faghat dar mahsoolat daste bandi namayesh dade mishavad(relation faale shode) baraye namayesh dar safeye asli bayad b panele modiriati ezafe shavad:

admin.site.register(models.ProductCategory,ProductCategoryAdmin)

#ertebate yek b yek:(class bayad tarif shavad bala)

admin.site.register(models.ProductInformation,ProductInfoAdmin)

#chand b chand:(class bayad tarif shavad bala)

admin.site.register(models.ProductTag,ProductTagAdmin)