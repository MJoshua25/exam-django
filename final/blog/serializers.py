from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from . import models


class CommentaireSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Commentaire
        fields = '__all__'


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    commentaires = CommentaireSerializer(many=True, required=False)

    class Meta:
        model = models.Article
        fields = '__all__'


class TagSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = models.Tag
        fields = '__all__'


class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = models.Categorie
        fields = '__all__'