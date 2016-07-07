from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["full_name", "email"]
		# exclude = [""] # use sparingly

	# clean_fieldname overriding
	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		# custom validation
		# if domain != "ioe":
		# 	raise forms.ValidationError("Please enter a IOE account.")
		if "edu" != extension:
			raise forms.ValidationError("Please use a valid college email address(.edu)")
		return email
		# if we dont add form validations here, we can add over in the views.py

	def clean_full_name(self):
		fname = self.cleaned_data.get("full_name")
		# if len(fname.split(" "))<2:
		# 	raise forms.ValidationError("Please enter your full name.")
		return fname

# independent of model
class ContactForm(forms.Form):
	full_name = forms.CharField(required = False)
	email = forms.EmailField()
	message = forms.CharField() # or use formwidgets

	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	email_base, provider = email.split("@")
	# 	domain, extension = provider.split(".")
	# 	# custom validation