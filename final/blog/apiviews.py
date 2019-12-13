from rest_framework import viewsets,filters

from . import serializers, models

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class CommentaireViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Commentaire.objects.all()
    serializer_class = serializers.CommentaireSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class TagViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Categorie.objects.all()
    serializer_class = serializers.CategorieSerializer