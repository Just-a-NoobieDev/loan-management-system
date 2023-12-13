from django.contrib import admin
from .models import Person, Loan, Payment


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'picture', 'document')


admin.site.register(Person, PersonAdmin)
admin.site.register(Loan)
admin.site.register(Payment)
