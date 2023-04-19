from django import template
from women.models import *

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('women/list_posts.html')
def show_posts(count=3, cat_id=None):
    if cat_id:
        posts = Women.objects.filter(cat_id=cat_id).order_by('-time_create')[:count]
    else:
        posts = Women.objects.all().order_by('-time_create')[:count]

    return {"posts": posts}

    
