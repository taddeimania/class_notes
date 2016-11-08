from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

from app.models import Click
import time
import random


class IndexView(View):

    def get(self, request):
        Click.objects.create()
        return HttpResponse(str(Click.objects.count()))
