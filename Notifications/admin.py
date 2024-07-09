from django.contrib import admin
from .models import Incubation,Inquiry,ReachOut
# Register your models here.

class ReadOnlyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)        
        return actions
    
admin.site.register(Incubation,ReadOnlyModelAdmin)
admin.site.register(ReachOut,ReadOnlyModelAdmin)
admin.site.register(Inquiry,ReadOnlyModelAdmin)
