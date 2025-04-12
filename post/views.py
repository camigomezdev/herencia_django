from django.shortcuts import render, get_object_or_404

from .models import Post, TextPost, ImagePost


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.post_type == 'text':
        post = TextPost.objects.get(pk=pk)
    elif post.post_type == 'image':
        post = ImagePost.objects.get(pk=pk)

    return render(request, 'post/detail.html', {'post': post})
