from django.shortcuts import render

def home(request):
	return render(request,'index.html')

def about(request):
	return render(request,'About.html')
		
def experience(request):
	return render(request,'Experience.html')

def portfolio(request):
	return render(request,'Portfolio.html')

def services(request):
	return render(request,'Services.html')
		
def contact(request):
	return render(request,'Contact.html')
		