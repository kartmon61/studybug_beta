from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Student, Comment, Category, License
from django.contrib.auth.models import User
from django.core.paginator import Paginator

#from .forms import PostForm

# Create your views here.

def Post(request):
    category_id = request.GET.get('category')
    # print("카테고리"+category_id)
    category = get_list_or_404(Category,code_no=category_id)
    comm_cnt = []
    try :
        posts = get_list_or_404(Student,category=category_id)
    
    #페이지화
        paginator = Paginator(posts,5) 
        page = request.GET.get('page')
        page_posts = paginator.get_page(page)
        return render(request,'list.html',{'page_posts':page_posts})
    except :
        posts = None
        return render(request,'list.html')

def Mpost(request):
    category_id = request.GET.get('category')
    print("카테고리"+category_id)
    category = get_list_or_404(Category,code_no=category_id)
    comm_cnt = []
    try :
        posts = get_list_or_404(Student,category=category_id)
        for i in posts:
            one_post = get_object_or_404(Student,id=i.id)
            comments = one_post.comment_set.all()
            comm_cnt.append(len(comments))

        #페이지화
        paginator = Paginator(posts,5) 
        page = request.GET.get('page')
        page_posts = paginator.get_page(page)
        return render(request,'list.html',{'page_posts':page_posts,'comm_cnt':comm_cnt})
    except :
        posts = None
        return render(request,'list.html')


def PostNew(request):
        if request.method == 'POST': 
                Student.license_on = request.POST['license']
                Student.category = request.POST['category']
                Student.body = request.POST['body']
                Student.rate = request.POST['rate']
                Student.author = request.user
                Student.save()
                return redirect('/post')
        else:
            category = Category.objects.all()
            license_on = License.objects.all()
            return render(request, 'create.html',{'category':category,'license':license_on})
                

def PostShow(request,post_id):
    one_post = get_object_or_404(Student,id=post_id)
    comments = one_post.comment_set.all()
    return render(request,'detail.html',{'posts':one_post,'comment':comments})

def PostEdit(request, post_id):
    if request.method == "POST":
        #수정 저장
        one_post = Student.objects.get(pk = post_id)
        one_post.license_on = request.POST['license']
        one_post.category = request.POST['category']
        one_post.body = request.POST['body']
        one_post.rate = request.POST['rate']
        one_post.author = request.user
        one_post.save()

        return redirect('/post/show/'+str(one_post.id))

    else:
        #수정 입력
        one_post = Student.objects.get(pk = post_id)
        return render(request, 'edit.html', {'posts' : one_post})


def PostDelete(request, post_id):
    one_post = Student.objects.get(pk = post_id)
    one_post.delete()
    return redirect('/post')


def commentcreate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Student,id=post_id)
        one_post.comment_set.create(text=request.POST['comment_content'],author=request.POST['comm_nm'])
    return redirect('/post/show/'+str(post_id))

def commentdelete(request,post_id,comment_id):
        one_comment = get_object_or_404(Comment,id=comment_id,student=post_id)
        one_comment = get_object_or_404(Comment,id=comment_id,student=post_id)
        one_comment.delete()
        return redirect('/post/show/'+str(post_id))

def redirectForm(request,msg):
        return render(request, 'redirect.html', {'msg': msg})


# def PostUpdate(request,post_id):
#     if(request.method == 'POST'):
#         one_post = get_object_or_404(Student,id=post_id)
#         one_post.title = request.POST['title']
#         one_post.content = request.POST['content']
#         one_post.save()

#         return redirect('/post/show/'+str(one_post.id))




# class PostView(ListView):   #html 템플릿 : 블로그 리스트를 담은 html : (소문자모델)_list.html
#     template_name = 'post/list.html'
#     context_object_name = 'comm_list'
#     model = Student

# class PostCreate(CreateView): #html : form (입력공간ß을 갖고 있는 html : (소문자모델)_form.html
#     template_name = 'post/create.html'
#     model = Student
#     #form_class = PostForm
#     fields = ['license_on','body','rate']
    
#     success_url = reverse_lazy('list')

# class PostDetail(DetailView): #html : 상세 페이지를 담은 html : (소문자모델)_detail.html
#     template_name = 'post/detail.html'
#     context_object_name = 'comm_post'
#     model = Student

# class PostUpdate(UpdateView): #html : form (입력공간)을 갖고 있는 html : (소문자모델)_form.html
#     template_name = 'post/create.html'
#     model = Student
#     fields = ['license_on','body','rate']
#     success_url = reverse_lazy('list')

# class PostDelete(DeleteView): #html : 삭제 확인 html (소문자모델)_confirm_delete.html
#     template_name = 'post/delete.html'
#     model = Student
#     success_url = reverse_lazy('list')

#######################################################################

# class CommentUpdate(UpdateView):
#     model = Comment
#     fields = ['text']
#     context_object_name = 'comment_update'
#     template_name = 'post/comment_update.html'

#     def dispatch(self, request, *args, **kwargs):
#         object = self.get_object()
#         if object.author != request.user:
#             messages.warning(request, '수정할 권한이 없습니다.')
#             return HttpResponseRedirect('/')
#             # 삭제 페이지에서 권한이 없다! 라고 띄우거나
#             # detail페이지로 들어가서 삭제에 실패했습니다. 라고 띄우거나
#         else:
#             return super(CommentUpdate, self).dispatch(request, *args, **kwargs)

# class CommentDelete(DeleteView):
#     model = Comment
#     template_name = 'post/comment_delete.html' 
#     success_url = '/'

#     def dispatch(self, request, *args, **kwargs):
#         object = self.get_object()
#         if object.author != request.user:
#             messages.warning(request, '삭제할 권한이 없습니다.')
#             return HttpResponseRedirect('/')
#         else:
#             return super(CommentDelete, self).dispatch(request, *args, **kwargs)