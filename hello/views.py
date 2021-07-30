from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import time

def rsa_computation(limit):
    p = 178542003245811211274167228297361192303886321036074276889145691522634525820185614278499562592134188995169731066418203258297035264969457638591284906658912408319763156912951486020761069099132619194489006875108217247513715271974383296142805846405783845170862140174184507256128825312324419293575432423822703857091;
    r = 187;
    for i in range(limit):
          p=(p*p)%r
    return p

# Create your views here.
def index(request):
    start_time = time.time()
    id = int(request.GET.get('id','0'))
    rsa_computation(id)
    return HttpResponse ("total time  taken = %s miliseconds\n" % ((time.time() - start_time)*1000))


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
