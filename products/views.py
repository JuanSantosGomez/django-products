from django.shortcuts import render
from rest_framework import views
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.serializers import ProductSerializer
from products.models import Product
from fileSculpt.filesculpt import Sculptfile
import os

# Create your views here.
class PostMultiple(APIView):
    def post(self, request, format=None):

        rejected = []
        accepted = []
        for req in request.data:

            serializer = ProductSerializer(data=req)

            if serializer.is_valid():
                serializer.save()
                accepted.append(serializer.data)
            else:
                rejected.append(serializer.data)
        if len(rejected) == 0:
            return Response(accepted, status=status.HTTP_201_CREATED)
        elif len(accepted) == 0:
            return Response(rejected, status=status.HTTP_400_BAD_REQUEST)
        return Response(rejected, status=status.HTTP_207_MULTI_STATUS)
