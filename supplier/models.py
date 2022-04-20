from __future__ import annotations
from distutils.command.upload import upload
import imp
from operator import mod
from tkinter import CASCADE
from django.urls import reverse
from django.db import models
from numpy import product
from sqlalchemy import true
from category.models import Category
#from store.models import Product
import store.models as stm
# Create your models here.

class supplier(models.Model):

    supplier_ID = models.IntegerField( primary_key= True, unique= True)
    supplier_name = models.TextField(max_length=200)

class supplied(models.Model):

    supplied_pk = models.AutoField(primary_key= True)
    supplier_id = models.ForeignKey('supplier', on_delete=models.CASCADE)
    product_id = models.ForeignKey(stm.Product, on_delete=models.CASCADE)
    supplied_qnt = models.IntegerField()




