from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                count += 1
        if count == 0:
            raise ValidationError('Assign is_main')
        elif count > 1:
            raise ValidationError('Is_main should be one tag')
        return super().clean()
    
class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInLine]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['name']


