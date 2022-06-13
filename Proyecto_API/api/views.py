#from django.shortcuts import render
from django.views import View
from .models import Company
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, resquest,id=0):
        if (id>0):
            companies=list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company=companies[0]
                datos = {'message':"Success", 'companies':company}
            else:
                datos = {'message':"Companies not found..."}
            return JsonResponse(datos)
        else:
            companies= list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message':"Success", 'companies':companies}
            else:
                datos = {'message':"Companies not found..."}
            return JsonResponse(datos)

    def post(self, resquest):
        #print(resquest.body)
        jd=json.loads(resquest.body)
        #print(jd)
        Company.objects.create(name= jd['name'], website= jd['website'], foundation= jd['foundation'])
        datos = {'message':"Success"}
        return JsonResponse(datos)

    def put(self, resquest, id):
        jd=json.loads(resquest.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company=Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Companies not found..."}
        return JsonResponse(datos)

    def delete(self, resquest, id):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Companies not found..."}
        return JsonResponse(datos)