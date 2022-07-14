from django.shortcuts import render,get_object_or_404,redirect  #use to render response
from blog.models import Post, Comment # these are model of particular App's
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin # it is use to check if user is logged in or not before access particular function whcih require login
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)   #it is CBV class based view proccess to do crud operation
from django.urls import reverse_lazy #it is use to return back after successfull or failed process
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/blog/post_list.html'
    model = Post

    def get_queryset(self):
        """
        here query w'll be in a filter() and after that
        their will be order_by function
        """
        return Post.objects.filter(published_date__isnull = True).order_by('create_date')





#########################################################
#########################################################

@login_url
def post_publish(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk)
    if request.method == 'post':
        form  = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = commentForm()
    return render(request, 'blog/comment_form.html',{'form' :form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_delete(request,pk):
    comment = get_object_or_404(Comment,pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
