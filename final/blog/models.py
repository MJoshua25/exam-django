from django.db import models
from tinymce import HTMLField
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Timemodel(models.Model):
    """Model definition for timemodel."""

    # TODO: Define fields here
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for timemodel."""

        abstract =True


class Categorie(Timemodel):
    """Model definition for Categorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50, unique=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom


class Tag(Timemodel):
    """Model definition for Tag."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50, unique=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.nom


class Article(Timemodel):
    """Model definition for Article."""

    # TODO: Define fields here
    titre = models.CharField(max_length=50, unique=True)
    titre_slug = models.SlugField()
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, related_name='articles', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='articles')
    cover = models.ImageField(upload_to='article/image')
    add_by = models.ForeignKey(User, verbose_name="Ajouter par", related_name='articles', on_delete=models.CASCADE)
    contenu = HTMLField('contenu')

    class Meta:
        """Meta definition for Article."""
        ordering = ['-date_add']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def save(self, *args, **kwargs):
        self.titre_slug = slugify(self.titre)
        super(Article, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre


class Commentaire(Timemodel):
    """Model definition for Commentaire."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    article = models.ForeignKey(Article, related_name='commentaires', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    message = models.TextField()

    class Meta:
        """Meta definition for Commentaire."""
        ordering = ['-date_add']
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return "{}: {}".format(self.nom, self.message)
