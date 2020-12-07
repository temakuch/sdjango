from django.shortcuts import render
from django.http import HttpResponse

def showposts(request):
	if request.method == 'GET':
		return HttpResponse('<h1>BLOG page</h1>')

def shrek(request):
	if request.method == "GET":
		return HttpResponse('''<h1>SHREK DANCER</h1>
							<a href = "https://www.youtube.com/watch?v=H-jSBAzbEmQ&ab_channel=PeacockKids" ''')
