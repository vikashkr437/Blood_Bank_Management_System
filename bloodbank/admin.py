from django.contrib import admin
from bloodbank.models import bloodbank, blood, hospital, order, donor,  employee
# Register your models here.


admin.site.register(bloodbank)
admin.site.register(blood)
admin.site.register(hospital)
admin.site.register(donor)
admin.site.register(employee)
admin.site.register(order)
