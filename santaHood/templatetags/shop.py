from django import template
from django.conf.urls.static import static
from django.templatetags.static import static

from ..models import Product

register = template.Library()

@register.simple_tag
def getLeagues():
    leagues = Product.objects.filter(quantity=1)
    lgs = []
    for leagueObj in leagues:
        league = {
            "id": leagueObj.id,
            "name": leagueObj.name,
            "url": static('img/emblem/league/scaled/league_' + str(leagueObj.id) + '.png')
        }
        lgs.append(league)
    return lgs