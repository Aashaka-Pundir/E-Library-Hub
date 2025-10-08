from django.shortcuts import render, redirect, get_object_or_404
from .models import Story, Category
from .forms import StoryForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Q

def home(request):
    stories = Story.objects.filter(published=True).order_by('-created_at')
    categories = Category.objects.all()
    query = request.GET.get('q')
    if query:
        stories = stories.filter(
            Q(title_icontains=query) | Q(contenticontains=query) | Q(categoryname_icontains=query)
        ).distinct()
    return render(request, 'stories/home.html', {'stories': stories, 'categories': categories})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk, published=True)
    return render(request, 'stories/story_detail.html', {'story': story})

@login_required
def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            messages.success(request, 'Story created successfully!')
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm()
    return render(request, 'stories/create_story.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'stories/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'stories/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
 