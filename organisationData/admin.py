from django.contrib import admin

# Register your models here.
from .models import OrgType, OrgAdmin
from .models import OrgRegBy
from .models import OrgData

admin.site.register(OrgType)
admin.site.register(OrgRegBy)
#admin.site.register(OrgData)

@admin.register(OrgData)

class OrgDataAdmin(admin.ModelAdmin):
    list_display = ('OrgID', 'OrgName', 'OrgType', 'OrgCreated')
    #ordering = ('name',)
    #search_fields = ('name', 'address', )


@admin.register(OrgAdmin)
class OrgAdminUser(admin.ModelAdmin):
    list_display = ('OAID', 'OAname', 'OAOrgName', 'OAJoinedDate')