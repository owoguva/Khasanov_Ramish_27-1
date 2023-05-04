from django.db.models import Q
from django.shortcuts import render, redirect
from posts.models import Post, Comment
from posts.forms import PostCreatForm, ReviewCreateForm
from posts.constants import PAGINATION_LIMIT
def main_page_view(requests):
    if requests.method == 'GET':
        context= {
            'user': requests.user
        }

        return render(requests, 'layouts/index.html', context=context)

def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)


        posts = posts[PAGINATION_LIMIT *(page-1):PAGINATION_LIMIT * page]

        if search:
            posts = posts.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search))

        context = {
            'posts': posts,
            'user': request.user,
            'pages': range(1, max_page+1)
        }
        return render(request, 'products/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == "GET":
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'form': ReviewCreateForm,
            'user': request.user
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        post = Post.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                post_id=id
            )
        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'form': ReviewCreateForm
        }
        return render(request, 'products/detail.html', context=context)

def post_create_view(request):
    if request.method == "GET":
        context = {
            'form': PostCreatForm
        }

        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = PostCreatForm(data, files)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')
            )
            return redirect('/posts/')
        return render(request, 'products/create.html', context={
            'form': form
        })

