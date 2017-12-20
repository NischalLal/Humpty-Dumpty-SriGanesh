from django.shortcuts import render
from .models import Post, Project, SocialSite, About, Contact

# Create your views here.

# Home
def home(request):
	return render(request, 'myblog/home.html', {})


def about(request):
	return render(request, 'myblog/about.html', {})


def project_list(request):
	return render(request, 'myblog/project_list.html', {})


def project_detail(request):
	return render(request, 'myblog/project_detail.html')


def post_list(request):
	return render(request, 'myblog/post_list.html', {})


def post_detail(request):
	return render(request, 'myblog/post_detail.html', {})


def contact(request):
	return render(request, 'myblog/contact.html')






