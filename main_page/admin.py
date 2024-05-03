from django.contrib import admin
from .models import Days
from django.db.models import QuerySet

# Register your models here.

admin.site.register(Days)













#
# class RatingFilter(admin.SimpleListFilter):
#     title = 'fff'
#     parameter_name = 'rating'
#
#     def lookups(self, request, model_admin):
#         return [
#             ('<40', 'плохой'),
#             ('>50', 'Норм')
#         ]
#
#     def queryset(self, request, queryset: QuerySet):
#         if self.value() == '<40':
#             return queryset.filter(rating__lt=40)
#
#
# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ['name', 'rating', 'year', 'budget', 'currency', 'director', 'ratingsss', ]
#     list_editable = ['rating', 'year', 'budget', 'currency', 'director']
#     ordering = ['-rating', '-year']
#     actions = ['set_dollars']
#     search_fields = ['name', 'year']
#     list_filter = ['year', RatingFilter]
#     filter_horizontal = ['actor']
#
#     @admin.display(description='Статус')
#     def ratingsss(self, movie):
#         if movie.rating > 1:
#             return 'Класс'
#
#     @admin.action(description='Установить значение в USD')
#     def set_dollars(self, request, qs: QuerySet):
#         qs.update(currency=Movie.USD)
#
# # сделать перевод в другую валюту при смене её в currency
