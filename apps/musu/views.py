from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from apps.nurbo import models
# Create your views here.
def index(request):
    works = models.Works.objects.all()
    return render(request, 'demo-academic.html', locals())
