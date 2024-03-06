from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Contact,Post
from django.http import HttpResponse
from django.http import HttpResponseRedirect, request
from .forms import ContactForm
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):

	featured = Post.objects.filter(featured = True)
	#latest = Post.objects.order_by('-timestamp')[0:3]
	post_list = Post.objects.all().order_by("id")
	
	paginator = Paginator(post_list, 3)
	#page_request_var = 'page'
	page = request.GET.get('page')
	#paged_post = paginator.get_page(page)
	try:
		paged_post = paginator.page(page)
	except PageNotAnInteger:
		paged_post = paginator.page(1)
	except EmptyPage:
		paged_post= paginator.page(paginator.num_pages)

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			c = form.save(commit=False)
			c.name = request.POST.get('name')
			c.email = request.POST.get('email')
			c.subject = request.POST.get('subject')
			c.msg = request.POST.get('msg')
			c.save()
			messages.success(request, 'Your messages submitted')
			return render(request, 'pages/index.html')

		else:
			messages.warning(request, 'please fill the form')
			return render(request, 'pages/index.html')
	else:
		form = ContactForm

	context = {
		'featured': featured,
		#'latest': latest,
		'form': form,
		#'post_list': paginated_queryset,
		#'page_request_var': page_request_var,
		'post_list': paged_post,
	}
	return render(request, 'pages/index.html', context)
def feature(request):
	featured = Post.objects.filter(featured = True)
	posts = Post.objects.all().order_by("id")
	
	paginator = Paginator(posts, 6)
	#page_request_var = 'page'
	page = request.GET.get('page')
	#paged_post = paginator.get_page(page)
	try:
		paged_post = paginator.page(page)
	except PageNotAnInteger:
		paged_post = paginator.page(1)
	except EmptyPage:
		paged_post = paginator.page(paginator.num_pages)


	context = {
		#'paginator': paginator,
		'featured': featured,
		'posts': paged_post,
	}

	return render(request, 'pages/feature.html',context)


def post(request,slug):
	post = Post.objects.filter(slug=slug)
	if post.exists():
		post = post.first()
	else:
		HttpResponse("<h3>page not found</h3>")
	context = {

		'post': post,
			
	}
	return render(request, 'pages/post.html', context)