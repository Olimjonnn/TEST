from importlib.resources import read_text
from itertools import product
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets 
from rest_framework.decorators import action, permission_classes, authentication_classes,api_view
from main.serializer import *
from main.models import *


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request):
        try:
            name = request.POST.get("name")
            Category.objects.create(name=name)
            return Response({"Created"})
        except Exception as arr:
            data = {
                "status":False,
                "error": f"{arr}"
            }
            return Response(data)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request):
        try:
            name = request.POST.get("name")
            category_id = request.POST.get("category")
            price = request.POST.get("price")
            barcode = request.POST.get("barcode")
            Product.objects.create(name=name, category_id=category_id, price=price, barcode=barcode)
            return Response({"Created"})
        except Exception as arr:
            data = {
                "status":False,
                "error": f"{arr}"
            }
            return Response(data)
    @action(["GET"], detail=False)
    def filter_category(self, request):
        category = request.GET.get("category")
        a = self.queryset.filter(category_id=category)
        pro = ProductSerializer(a, many=True)
        return Response(pro.data)

class ProductItemView(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

    def create(self, request):
        try:
            product_id = request.POST.get("product")
            deliver_id = request.POST.get("deliver")
            base_price = int(request.POST.get("base_price"))
            price = int(request.POST.get("price"))
            expired = request.DATE.get("expired")
            quantity = int(request.POST.get("quantity"))
            Product.objects.create(product_id=product_id, deliver_id=deliver_id, base_price=base_price, price=price, expired=expired, quantity=quantity)
            return Response({"Created"})
        except Exception as arr:
            data = {
                "status":False,
                "error": f"{arr}"
            }
            return Response(data)

    @action(["GET"], detail=False)
    def filter_category(self, request):
        try:
            user = request.GET.get("category")
            product = Product.objects.get(category_id=user)
            quan = 0
            price = 0
            b = []
            for i in product:
                quan += i.quantity
                price += i.price*i.quantity
                dt = {
                    'product name': i.product.name,
                    'client name': i.client.name,
                    'quantity': i.quantity,
                    'summa': i.price
                }
                b.append(dt)
            data = {
                'total sailed': quan,
                'total summa': price,
                'products': b
            }
            return Response(data)
        except Exception as arr:
            dat = {
                "error": f"{arr}"
            }
            return Response(dat)
            

class DeliverView(viewsets.ModelViewSet):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer

    def create(self, request):
        try:
            name = request.POST.get("name")
            phone = int(request.POST.get("phone"))
            address = request.POST.get("address")
            Deliver.objects.create(name=name, phone=phone, address=address)
            return Response({"Created"})
        except Exception as arr:
            data = {
                "status":False,
                "error": f"{arr}"
            }
            return Response(data)

