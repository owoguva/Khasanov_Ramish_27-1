from django.shortcuts import render
from posts.models import Post
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
