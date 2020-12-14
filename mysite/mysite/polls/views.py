from django.http import HttpResponse
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests



def index(request):
    url = "https://air-quality.com/place/india/delhi/a32ed7fc?lang=en&standard=aqi_us"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    val = soup.find("div", {"class": "pollutants"})
    c_name = val.findAll("div", {"class": "name"})
    v_name = val.findAll("div", {"class": "value"})

    result = dict()
    for i in range(len(c_name)):
        result[c_name[i].get_text()] = v_name[i].get_text()
    return JsonResponse({"data" : result})