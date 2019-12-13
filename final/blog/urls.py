from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from . import apiviews


router = DefaultRouter()
router.register('commentaire', apiviews.CommentaireViewSet, base_name='commentaire')
router.register('article', apiviews.ArticleViewSet, base_name='article')
router.register('tag', apiviews.TagViewSet, base_name='tag')
router.register('categorie', apiviews.CategorieViewSet, base_name='categorie')




urlpatterns = [
    path('', views.index, name="index"),
    path('tag/<str:nom>', views.tag, name="tag"),
    path('category/<str:nom>', views.categorie, name="categorie"),
    path('detail/<slug:titre>', views.detail, name="detail"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
]

urlpatterns += router.urls