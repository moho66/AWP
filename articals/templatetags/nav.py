from django.template import Library
from articals.models import Category

register=Library()

@register.inclusion_tag('cats.html')
def cats():
    return {"cat_menu":Category.objects.all()}