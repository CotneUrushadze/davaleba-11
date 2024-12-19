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



class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):


        print(Category.objects.with_item_count())
        
        # print(Item.objects.with_tag_count())

        # print(Tag.objects.popular_tags(19))