from django.shortcuts import render
from app.models import *
from app.serialzers import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Create your views here.

class productcrud(ViewSet):
    def list(self,request):
        PDO=product.objects.all() #orm
        PJO=productModelserializers(PDO,many=True) #json
        return Response(PJO.data)
    
    def retrieve(self,request,pk):
        PO=product.objects.get(pk=pk)
        JPO=productModelserializers(PO)
        return Response(JPO.data)
    
    def create(self,request):
        JD=request.data
        PDO=productModelserializers(data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Data':'Data is crested'})
        else:
            return Response({'error':'data is invalid'})
    
    def Updata(self,request,pk):
        PO=product.objects.get(pk=pk)
        JD=request.data
        PDO=productModelserializers(PO,data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'error':'Not ABle To update'})

    def partial_update(self,request,pk):
        PO=product.objects.get(pk=pk)
        JD=request.data
        PDO=productModelserializers(PO,data=JD,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'error':'Not ABle To update'})

    def destroy(self,request,pk):
        product.objects.get(pk=pk).delete()
        return Response({'deleted':'Data is deleted'})
