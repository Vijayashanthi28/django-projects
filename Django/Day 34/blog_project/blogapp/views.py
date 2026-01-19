from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogapp/blog_list.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        content = request.POST.get('comment')
        if content:
            Comment.objects.create(blog=blog, content=content)
        return redirect('blog_detail', blog_id=blog.id)

    return render(request, 'blogapp/blog_detail.html', {'blog': blog})
