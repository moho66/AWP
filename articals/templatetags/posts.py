from django.template import Library
from articals.models import Artical

register=Library()


@register.inclusion_tag('pup_posts.html')
def pupPosts():
    articlas=Artical.objects.all().order_by('-views')[:3]
    return {'articlas':articlas}