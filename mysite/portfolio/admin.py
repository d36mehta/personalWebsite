from django.contrib import admin
from .models import TextBubble, Resume, Quotes, Languages


# Register your models here.
class LanguageInLine(admin.TabularInline):
    model = Languages
    extra = 1


class TextBubbleAdmin(admin.ModelAdmin):
    fields = ['tag', 'name', 'text', 'picture', 'links', 'pub_date']
    list_display = ('tag', 'name', 'pub_date')
    list_filter = ['tag']
    inlines = [LanguageInLine]


admin.site.register(TextBubble, TextBubbleAdmin)
admin.site.register(Resume)
admin.site.register(Quotes)
