from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser

class CategoryDorilar(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_dorilar'

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name

class Dorilar(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(CategoryDorilar, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dorilar/', default='default_img/default_dori_img.png')
    page = models.IntegerField()
    dori_lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'dorilar'

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class DoriAuthor(models.Model):
    dori = models.ForeignKey(Dorilar, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'dori_author'

    def __str__(self):
        return f'{self.dori.title} - {self.author.first_name} {self.author.last_name}' if self.dori else f'Unknown Dori - {self.author.first_name} {self.author.last_name}'

class Review(models.Model):
    comment = models.CharField(max_length=200)
    star_given = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    dori = models.ForeignKey(Dorilar, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'{self.star_given} - {self.dori.title} - {self.user.username}'
