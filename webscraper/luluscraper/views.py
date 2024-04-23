from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from django.views.decorators.cache import cache_page

URLs = ["https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json","https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"]
"""
  This view function is responsible for extracting product information
  by scraping the provided URLs. 
  
  Parameters:
  - request: HTTP request object. 
  Returns:
  - JsonResponse object containing the URL scraped, the list of 
    product.displayName values extracted in JSON format
    If the URL cannot be scraped or no product information is found,
    an appropriate error message is returned.
 
  Note: This function assumes that the URL provided in the request
  is accessible and contains JSON content with product.displayName
  information structured in a predictable manner.
 
  Example usage:
 
    GET /scrape
 
  Response:
  {
  "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json": {
    "product.displayName": [
      [
        "Wunder Train High-Rise Tight 25\""
      ],
      [
        "lululemon Align™ High-Rise Pant 28\""
      ].......
    }               
"""
#cache the page for 15 minutes
@cache_page(60 * 15)
def scrape(request):
    result= {}
    try:
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
    except ValueError:
        return JsonResponse({"Scraping Error": "Data not found or URL broken"}, status=404)
