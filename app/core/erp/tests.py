#from django.test import TestCase
from config.wsgi import *
from core.erp.models import Type

# List
# query = Type.objects.all()
# print(query)

# Insert
#Type(name = 'Accionista').save()
#Type(name = 'Presidente').save()

# Update
# t = Type.objects.get(pk=1)
# t.name = 'Accionistas'
# t.save()

# Delete
# t = Type.objects.get(pk=1)
# t.delete()

obj = Type.objects.filter(name__icontains='pre')
print(obj)