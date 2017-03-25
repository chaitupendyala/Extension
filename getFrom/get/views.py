from django.shortcuts import render
from django.http import HttpResponse
from .models import Our_database
from django.views.decorators.csrf import csrf_exempt
from .models import Our_database

global prev
prev = ['','']

@csrf_exempt
def index(request):
	global prev
	if request.method == 'POST':
		url = request.POST['url']
		time = request.POST['time']
		tab_id = request.POST['tabid']
		'''if prev == ['','']:
			a = Our_database(url = url,prev_url=prev[0],time = time)
			prev = [str(url),str(tab_id)]
			a.save()
		elif prev != [str(url),str(tab_id)]:
			a = Our_database(url = url,prev_url=prev[0],time = time)
			prev = [str(url),str(tab_id)]
			a.save()
		else:
			pass'''
	else:
		url = "hello"
	return HttpResponse("<h1>Added"+url+"</h1>")

def show(request):
	return render(request,'get/show.html',{'db':Transition.objects.all()})
