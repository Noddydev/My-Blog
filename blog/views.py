from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
#post_data=[
    #{
        #'Author':'Vonn',
       # 'Title':'Python',
      #  },
    #{
     #   'Author':'Dannis',
    #    'Title':'C',
   #     },
  #  ]
def home(request):
    #return HttpResponse("<h1>My_Blog-Home Page</h1>")
    context={'posts':Post.objects.all(),'Title':'Django Project-'}
    return render(request,'blog/home.html',context)
	
class PostDetailView(DetailView):
	model=Post
	
class PostCreateView(LoginRequiredMixin,CreateView):
		model=Post
		fields=['title','content']
		def form_valid(self,form):
			form.instance.author=self.request.user
			return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
		model=Post
		fields=['title','content']
		def test_func(self):
			post=self.get_object()
			if self.request.user==post.author:
				return True
			return False	

		def form_valid(self,form):
			form.instance.author=self.request.user
			return super().form_valid(form)
			

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
		model=Post
		success_url='/'
		def test_func(self):
			post=self.get_object()
			if self.request.user==post.author:
				return True
			return False				
		
def about(request):
    return render(request,'blog/about.html')
