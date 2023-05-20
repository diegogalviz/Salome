"""
Cuando no se configuran las variables del sistema para que reconozca los modulos de python entonces se agregan estas lineas que vienen acontinuacion
import sys
sys.path.append('../../')
"""

# from django.test import TestCase
from salome.wsgi import *
from app1.models import *

# Create your


# listar


t=Type_employee()
t.name = 'presidente'
t.save()

query = Type_employee.objects.all()
print(query)
