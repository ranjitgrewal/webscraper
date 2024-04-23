from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from django.views.decorators.cache import cache_page

# Create your views here.
URLs = ["https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json","https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"]

#cache the page for 15 minutes
@cache_page(60 * 15)
def scrape(request):
    result= {}
    for URL in URLs:
        data=[]
        prod_dict={}
        page = requests.get(URL)
        json_object = json.loads(page.text)
        for content in json_object["contents"]:
            for mcontent in content["mainContent"]:
                if "contents" not in mcontent.keys():
                    continue 
                for mc in mcontent["contents"]:
                    for rec in mc["records"]:
                        data.append(rec["attributes"]["product.displayName"])
        result[URL]={"product.displayName":data}
    return JsonResponse(result)
