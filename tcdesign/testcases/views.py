from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Testcase

# Create your views here.
def index(request):
    latest_testcase_list = Testcase.objects.order_by('-last_update')[:5]
    context = {'latest_testcase_list': latest_testcase_list}
    return render(request, 'testcases/index.html', context)

def detail(request, testcase_id):
    return HttpResponse(f"You're looking at testcase {testcase_id}.")
