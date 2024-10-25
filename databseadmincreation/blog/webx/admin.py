from django.contrib import admin
# from .models import chaiVariety
# from .models import ChaiReview
# from . models import Cirtificate
# from. models import Store
# # Register your models here.
# admin.site.register(chaiVariety)
# admin.site.register(ChaiReview)
# admin.site.register(Cirtificate)
# admin.site.register(Store)
from . models import chaiVariety,ChaiReview, Cirtificate,Store
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2
class chaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','date_added')
    inlines = [ChaiReviewInline]
class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal = ('chai_Varities',)
class CirfiticateAdmin(admin.ModelAdmin):
    list_display = ('chai',)


admin.site.register(chaiVariety,chaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Cirtificate,CirfiticateAdmin)