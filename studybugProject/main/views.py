from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from post.models import Student, Comment

# Create your views here.
def main(request):
    posts = Student.objects.all().order_by('-id')
    paginator = Paginator(posts,5)  
    page_posts = paginator.get_page(1)
    category_no = request.GET.get('category_no')
    if category_no is not None:
        redirect('post')
    return render(request,'main.html',{'rlist':page_posts})
 
