from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import timezone
from django.shortcuts import redirect
from .forms import UserForm, LoginForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	print(posts)
	return render(request, 'blog/home.html', {'posts': posts})
##auth 
def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid(): 
			new_user = User.objects.create_user(**form.cleaned_data)
			return redirect('login')
	else:
		form = UserForm()
	return render(request, 'blog/user/signup.html', {'form': form})

def signin(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			return HttpResponse('로그인 실패. 다시 시도 해보세요.')
	else:
		form = LoginForm()
	return render(request, 'blog/user/login.html', {'form': form})
## post
def post_list(request):
	contents = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	paginator = Paginator(contents, 2)
	pnm = request.GET.get("page")	
	try:
		page = paginator.page(pnm)		
	except PageNotAnInteger: #페이지 번호가 정수가 아닐때 1페이지를 보여줌.
		page = paginator.page(1)
	except EmptyPage:		#영역을 벗어났을때 마지막 페이지를 보여줌...  
		page = paginator.page(paginator.num_pages)
	print(page)
	print(page.has_next())
	print(page.has_previous())
	print(page.next_page_number())
	print()
	return render(request, 'blog/post_list.html', {'page': page})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False) ##넘겨진 데이터를 바로 저장하지 말라는 뜻 
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post) ##추가하고자 하는 글의 Post모델 인스턴스를 가져옴 
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
		return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})