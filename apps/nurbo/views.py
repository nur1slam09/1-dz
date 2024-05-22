from django.shortcuts import render


from apps.nurbo import models
# Create your views here.
def index(request):
    about = models.About.objects.latest('id')
    academic = models.Academic.objects.all()
    return render(request, 'demo-academic.html', locals())
