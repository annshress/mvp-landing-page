from django.shortcuts import render

# Create your views here.
# how each page is going to look like
# REQUEST AND RESPONSE
# directed from urls.py

def about(request):
	context = {
	}
	return render(request, "about.html", context)
