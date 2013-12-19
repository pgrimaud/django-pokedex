from django.template import Context, loader
from pokemon.models import Pokemon
from django.http import HttpResponse
from django.http import Http404

def index(request):
    Pokemons = Pokemon.objects.all().order_by('id_pokemon')
    t = loader.get_template('pokemon/index.html')
    c = Context({
        'Pokemons': Pokemons,
    })
    return HttpResponse(t.render(c))

def pokemon(request, id):
    try:
        Pkmn = Pokemon.objects.get(id_pokemon=id)
    except Pokemon.DoesNotExist:
        raise Http404
    return HttpResponse(loader.get_template('pokemon/pokemon.html').render(Context({'Pokemon': Pkmn,})))