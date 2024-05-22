from django.contrib import admin
from .models import Review, Dorilar, Author, CategoryDorilar, DoriAuthor, Language

admin.site.register(Author)
admin.site.register(CategoryDorilar)
admin.site.register(Dorilar)
admin.site.register(DoriAuthor)
admin.site.register(Review)
admin.site.register(Language)
