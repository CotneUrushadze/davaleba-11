from typing import Any
from django.core.management.base import BaseCommand
from django.db.models import (
    Count,
    Max,
    Min,
    Avg,
    Sum,
    

)
from shop.models import Tag, Category, Item



# class Command(BaseCommand):
#     def handle(self, *args: Any, **options: Any):
      


# #N1 
#         item_count = Category.objects.aggregate(item_count=Count('items'))
#         print(item_count)


# #N2
#         prices = Item.objects.aggregate(
#             min_price = Min('price'),
#             max_price = Max('price'),
#             avg_price = Avg('price')
#         )
#         print(prices)



# #N3
#         categories = Category.objects.annotate(
#             quantity=Count('items'),
#             price_sum=Sum('items__price', default=0 )
#             )
        
#         for category in categories:
#             print(f"{category.name} : {category.quantity}, {category.price_sum}" )


# #N4
#         items = Item.objects.select_related('category').all()
#         for item in items:
#             print(f"{item.name}, {item.description} \n")



# #N5
#         items = Item.objects.select_related('category').all()
#         for item in items:
#             print(f"{item.name} : {item.category.name} \n")


# #N6
#         items = Item.objects.prefetch_related('tags').all()

#         for item in items:
#             tag_names = [tag.name for tag in item.tags.all()]
#             print(item.name, ", ".join(tag_names))        