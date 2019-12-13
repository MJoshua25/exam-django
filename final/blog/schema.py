import graphene
from graphene import relay, ObjectType , Connection , Node,Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from . import models
from django_filters import OrderingFilter
from django.contrib.auth.models import User


class ExtendConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection

class CategorieNode(DjangoObjectType):
   class Meta:
        model = models.Categorie
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection
    

class TagNode(DjangoObjectType):
    class Meta:
        model = models.Tag
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection


class ArticleNode(DjangoObjectType):
    class Meta:
        model = models.Article
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'categorie__nom':['exact'],
            'tags__nom':['exact'],
            'status': ['exact'],
        }
        order_by = OrderingFilter(
            fields=(
                ('date_add','date_add'),
            )
        )
        interfaces = (relay.Node, )
        connection_class = ExtendConnection


class CommentaireNode(DjangoObjectType):
    class Meta:
        model = models.Commentaire
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'article__titre':['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection



class Query(graphene.ObjectType):
    categorie = relay.Node.Field(CategorieNode)
    all_categorie = DjangoFilterConnectionField(CategorieNode)

    tag = relay.Node.Field(TagNode)
    all_tag = DjangoFilterConnectionField(TagNode)

    article = relay.Node.Field(ArticleNode)
    all_article = DjangoFilterConnectionField(ArticleNode)

    commentaire = relay.Node.Field(CommentaireNode)
    all_commentaire = DjangoFilterConnectionField(CommentaireNode)

