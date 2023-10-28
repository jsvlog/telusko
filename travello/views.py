from django.shortcuts import render
from .models import form

# Create your views here.
def index(request):
    addInfo = form()
    addInfo.addInfo = "ADDITIONAL INFO"
    addInfo.basicInfo = "BASIC INFO"
    return render(request, 'index.html',{'right': addInfo})