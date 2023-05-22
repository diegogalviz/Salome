"""
Cuando no se configuran las variables del sistema para que reconozca los modulos de python entonces se agregan estas lineas que vienen acontinuacion
import sys
sys.path.append('../../')
"""

'''
orm mapeo de objetos relacionales...
'''

# from django.test import TestCase


from salome.wsgi import *
from app1.models import *

# Create your


# _______________________________________________________________

# insercion
# try:
#     t = Type_employee()
#     t.name = 'mensajeria'
#     t.save()
# except Exception as e:
#     print(e)

# _______________________________________________________________

# listar
query = Client.objects.all()
print(query)
# _______________________________________________________________

# edicion
# t = Client.objects.get(id=1)
# t.name = 'presidente1'
# t.save()
# print(t)


# _______________________________________________________________
# eliminacion
# t= Client.objects.get(id=1)
# t.delete()

# _______________________________________________________________
'''
# llamar a los que cumplan un filtro es como usar like en sql
name__contains: tiene encuenta si son mayusculas o no
'''
query = Client.objects.filter(name__contains='se')
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
name__icontains: ignora si son mayusculas o no
'''
query = Client.objects.filter(name__icontains='ME')
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
name__startswith: buscar las que inicien por una letra
'''
query = Client.objects.filter(name__startswith='p')
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
name__endswith: buscar las que terminen por una letra 
'''
query = Client.objects.filter(name__endswith='o')
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
name__exact: buscar las coinsidencias que sean exactamente igual a
'''
query = Client.objects.filter(name__exact='presidente')
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
name__in: buscar las coinsidencias que esten dentro de una lista que le pasemos...
'''

query = Client.objects.filter(name__in=['presidente', 'mensajeria'])
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
.count: si agregamos esta funcion al final de query, podemos saber cuantos registros hay en el query...
'''

query = Client.objects.filter(name__in=['presidente', 'mensajeria']).count()
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
.query: si agregamos esta funcion al final del query, podemos saber la sentencia sql que esta utilizando
'''

query = Client.objects.filter(name__contains='pre').query
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
.exclude: si agregamos esta funcion al final del query, 
podemos coloacar elementos que no queramos tener en cuenta en el analisis del query
'''

query = Client.objects.filter(name__endswith='o').exclude(id=6)
print(query)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
podemos iterar mediante un for el query que hayamos escrito.
'''

query = Client.objects.filter(name__endswith='o')
for i in query:
    print(i.name)

# _______________________________________________________________

'''
# llamar a los que cumplan un filtro es como usar like en sql
[:2]podemos limitar el numero de registros traidos con la sintasis de listas de python al final de la lista a iterar
'''

query = Client.objects.filter(name__endswith='o')
for i in query[:2]:
    print(i.name)

    # _______________________________________________________________

    '''
    # llamar a los que cumplan un filtro es como usar like en sql
    [:2]podemos limitar el numero de registros traidos con la sintasis de listas de python al final de la lista a iterar
    '''

    query = Client.objects.filter(name__endswith='o')
    for i in query[:2]:
        print(i.name)