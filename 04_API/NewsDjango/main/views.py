from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import include, path
from django.core.serializers.json import Serializer


def index(request):

    context = {
        "page": "main",
        "category": "society",
        "title": "멈춰 선 주택 건설현장…고용장관 운송거부 철회해야",
        "time": "2022.12.1 16:34",
        "URL": "https://v.daum.net/v/20221201163447622"
    }

    # json = Serializer.serialize("json", context, fields=('page', 'category', 'title', 'time', 'URL'))
    
    return render(request, 'index.html', context) # index.html만 보임
    # return JsonResponse(context) # context가 Json 형식으로 보임
    # return render(json) # 되는지 모름
    # return HttpResponse("Hello, world. You're at the main page.")