from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Category, Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import CategoryModelForm, PostModelForm
from django.contrib import messages

# Create your views here.
def HomeView(request):
    featuredPosts = Post.objects.order_by('-id')[:3]
    post_lists = Post.objects.order_by('-id')
    categories = Category.objects.order_by('-id')

    paginator = Paginator(post_lists, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'featuredPosts' : featuredPosts,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'blog/home.html', context)



@login_required
def PostCreateView(request):
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Post created successfully')
        return redirect('blog:home')

    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Create Post'
    }

    return render(request, 'blog/post-form.html', context)


# New post detail view
def PostDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post-detail.html', context)



@login_required
def PostUpdateView(request, pk):
    post_id = get_object_or_404(Post, pk=pk)
    form = PostModelForm(request.POST or None, request.FILES or None, instance=post_id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Post updated successfully.')
        return redirect('blog:home')

    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Post'
    }

    return render(request, 'blog/post-form.html', context)


@login_required
def PostDeleteView(request, pk):
    query = get_object_or_404(Post, pk=pk)
    query.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('blog:home')


    

@login_required
def CategoryViewList(request):
    cat = Category.objects.order_by('-id')
    paginator = Paginator(cat, 5)
    page = request.GET.get('page')
    categories = paginator.get_page(page)

    context = {
        'categories' : categories
    }

    return render(request, 'blog/category.html', context)


@login_required
def CategoryUpdateView(request, pk):
    cat_id = get_object_or_404(Category, pk=pk)
    form = CategoryModelForm(request.POST or None, instance=cat_id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Category updated successfully.')
        return redirect('blog:category')


    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Category'
    }

    return render(request, 'blog/category-form.html', context)

        

@login_required
def CategoryDeleteView(request, pk):
    query = get_object_or_404(Category, pk=pk)
    query.delete()
    messages.success(request, 'Category deleted successfully')
    return redirect('blog:category')



@login_required
def CategoryCreateView(request):
    form = CategoryModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Category added successfully.')
        return redirect('blog:category')


    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Create Category'
    }

    return render(request, 'blog/category-form.html', context)


