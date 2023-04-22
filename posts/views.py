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


def post_detail_view(request, id):
    if request.method == "GET":
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all()
        }

        return render(request, 'products/detail.html', context=context)