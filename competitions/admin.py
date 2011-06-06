from models import (Competition, Judge, Brewer, Beer, Attribute, Rating, Entry,
        Result, JudgeRank)
from django.contrib import admin

admin.site.register(Attribute)
admin.site.register(Beer)
admin.site.register(Brewer)
admin.site.register(Competition)
admin.site.register(Judge)
admin.site.register(Rating)
admin.site.register(Entry)
admin.site.register(Result)
admin.site.register(JudgeRank)
