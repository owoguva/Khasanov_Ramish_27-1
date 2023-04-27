from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import PostCreatForm, ReviewCreateForm
def main_page_view(requests):
    if requests.method == 'GET':
        return render(requests, 'layouts/index.html')

def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'products/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == "GET":
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all()
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
def review_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ReviewCreateForm
        }
        return render(request, 'products/create.html', context=context)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ReviewCreateForm(data, files)

        if form.is_valid():
            Post.objects.create(
                text=form.cleaned_data.get('text'),
                product_id= form.cleaned_data.get('product')

            )

            return redirect('/posts/')

        return render(request, 'products/create.html', context={
            'form': form
        })
