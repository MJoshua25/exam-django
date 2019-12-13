from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.
@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    '''Admin View for Categorie'''

    list_display = (
        'nom',
        'date_add'
    )
    list_filter = (
        'date_add',
        )
    date_hierarchy = 'date_add'


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    '''Admin View for Tag'''

    list_display = (
        'nom',
        'date_add'
    )
    list_filter = (
        'date_add',
        )
    date_hierarchy = 'date_add'

@admin.register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    '''Admin View for Commentaire'''

    list_display = (
        'nom',
        'article',
        'email',
        'message',
        'date_add'
        )
    list_filter = ('article',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    '''Admin View for Article'''

    list_display = (
        'titre',
        'description',
        'categorie',
        'add_by',
        )
    list_filter = (
        'tags',
        'add_by',
        'categorie',
        )
    readonly_fields = ('titre_slug',)
    search_fields = ('titre',)
    date_hierarchy = 'date_add'