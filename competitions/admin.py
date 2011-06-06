from models import Competition, Judge, Brewer, Beer, Attribute, Rating
from django.contrib import admin

admin.site.register(Attribute)
admin.site.register(Beer)
admin.site.register(Brewer)
admin.site.register(Competition)
admin.site.register(Judge)
admin.site.register(Rating)
