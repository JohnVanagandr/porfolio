from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry
# Create your views here.

def queries(request):
  #Obtener todos los elementos de los autores
  authors = Author.objects.all()

  #Filtros en las busquedas por condiciones
  filtered = Author.objects.filter(email='psmith@example.org')

  #Obtener un unico objeto
  author = Author.objects.get(id=1)

  #Obtener los 10 primeros elementos
  limit = Author.objects.all()[:10]

  #Obtener los 5 valores saltando los 5 primeros valores 
  offsets = Author.objects.all()[5:10]

  #Obtener todos los elementos ordenados
  orders = Author.objects.all().order_by('email')

  #Obtener todos los elementos que su id sea menor o igual a 15
  # __lte: menor o igual (lower than equals)
  # __gte: mayor o igual (grester than equals)
  
  # __it: menor que (lower than)
  # __gt: mayor que (greater than)

  # __contains: contiene
  # __exact: exacto
  filtered = Author.objects.filter(id__lte=15)
  
  # Obtener los autores que contienen en su nombre la palabra (man)
  filtered = Author.objects.filter(name__contains='man')

  return render(request, 'post/queries.html',{
    'authors' : authors,
    'filtered' : filtered,
    'author': author,
    'limit' : limit,
    'offsets' : offsets,
    'orders' : orders})

  # return HttpResponse('consulta realizada')