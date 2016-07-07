from django.shortcuts import render

# Create your views here.
# how each page is going to look like
# REQUEST AND RESPONSE
# directed from urls.py

from .forms import SignUpForm , ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp
#import registration.models.RegistraionProfile
from .scrape import Extract

def home(request):
	title = "Newsletter"
	form = SignUpForm(request.POST or None)

	context = {
		"template_title" : title,
		"form" : form
	}

	if form.is_valid():
		# form.save()
		# print request.POST
		instance = form.save(commit = False)

		fname = form.cleaned_data.get("full_name")
		if not fname:
			fname = "hello dello"

		instance.full_name = fname

		instance.save()
		context = {
			"template_title" : "Thank You"
		}

	if request.user.is_staff:
		# how do i get models off the registration redux???
		#print RegistraionProfile.objects.all()
		queryset = SignUp.objects.all().order_by('-timestamp')
		# print queryset.count()
		context = {
			"queryset" : queryset
		}
	
	# context makes html pages more dynamic

	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	title_align_center = False

	if form.is_valid():
		# print form.cleaned_data
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")

		subject = "Site Contact Form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s : via %s == %s" %(
			form_message, 
			form_full_name, 
			form_email)
		html_message = """
		<h1> hi there! </h1>
		"""
		
		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, 
			html_message = html_message,
			fail_silently=False)
	
	context = {
		"form": form,
		"title_align_center": title_align_center,
	}

	return render(request, "contact.html", context)

def callMe():
	teams = ["portugal","wales","france"]
	games = Extract(teams)
	context = {
		"games" : games
	}
	return context
def feed(request):
	return render(request, "feed.html", callMe())

def refresh_feed(request):
	if request.GET.get('mybtn'):
		return render(request, "feed.html", callMe())
