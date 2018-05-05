# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎光临 自强学堂! WangDoo~")
