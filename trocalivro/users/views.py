from django.template import loader
from django.http import HttpResponse
from .models import User

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def db_test(request):
    user = User.objects.all().values()
    template = loader.get_template('database_test.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))
