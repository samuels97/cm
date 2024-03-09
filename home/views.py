from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, "index.html", context)

def aboutus(request):
    return

def Button(text: str, classNames: list[str])->str:
    css_class_string = " ".join(classNames)
    return f'<button class="{css_class_string}">{text}</button>'
