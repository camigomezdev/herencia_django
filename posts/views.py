from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'posts/detail.html', {'post': post})
