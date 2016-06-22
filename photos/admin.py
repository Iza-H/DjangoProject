from django.contrib import admin
from models import Photo



class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'licence', 'visibility')
    list_filter =  ('licence', 'visibility')
    search_fields = ('name', 'description')

    def owner_name(self, obj):
        return obj.owner.first_name + u' ' + obj.owner.first_name
    owner_name.short_description = u'Photo owner'
    owner_name.admin_order_field = 'owner'

    fieldsets = (
        (None, {
            'fields': ('name',),
            'classes': ('wide',)
        }),
        (
         'Description & Author', {
             'fields': ('description', 'owner'),
             'classes': ('wide',)
         }
        ),
        ('Extra', {
            'fields' : ('url', 'licence', 'visibility'),
            'classes': ('wide', 'collapse')
        })
    )



admin.site.register(Photo, PhotoAdmin)