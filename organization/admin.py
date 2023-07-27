from django.contrib import admin
from organization.models import Organization
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from user.models import User

class OrganizationResource(resources.ModelResource):
    owner = fields.Field(
        column_name='owner',
        attribute='owner',
        widget=ForeignKeyWidget(User, 'id')
    )
    class Meta:
        model = Organization

class OrganizationAdmin(ImportExportModelAdmin):
    resource_class = OrganizationResource

admin.site.register(Organization, OrganizationAdmin)
