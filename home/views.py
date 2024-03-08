#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")


def Button(text: str, classNames: List[str], onClick=None)->str:
    css_class_string = " ".join(classNames)
    return f'<button class="{css_class_string}">{text}</button>'
