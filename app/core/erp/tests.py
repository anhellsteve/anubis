#from django.test import TestCase
from config.wsgi import *
from core.erp.models import *

# LISTAR
for i in Category.objects.filter():
    print(i)

