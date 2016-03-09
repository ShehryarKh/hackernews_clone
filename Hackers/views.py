from django.shortcuts import render,redirect
from django.views.generic import View 
from .forms import PostForm,UserForm
from django.contrib.auth import authenticate, login
from .models import Posts
from django.shortcuts import get_object_or_404

# Create your views here.
class Register(View):
	template = "register.html"
	def get(self,request):
		register = False

		if request.user.is_authenticated():
			return redirect("index")
		userform = UserForm()
		context={
			"userform":userform
			}
		return render(request,self.template,context)



	def post(self,request):

		userform = UserForm(data=request.POST)
		if userform.is_valid():
			user = userform.save()
			return redirect("index")
		else:
			context={
			"userform":userform
			}
			return render(request,self.template,context)

class Login(View):





class Index(View):
	template = "index.html"

	def get(self,request):
		posts = Posts.objects.all()
		context= {
			"posts": posts
		}
		return render(request,self.template,context)

class Create(View):
    template = "create.html"

    def get(self,request):
        postform = PostForm

        context = {
            "form":postform
        }
        return render(request, self.template, context)

    def post(self,request):
        postform = PostForm(request.POST)

        if postform.is_valid():
            postform.save()
            return redirect("index")

class Edit(View):
	template = "edit.html"

	def get(self,request,slug):
		news = get_object_or_404(Posts,slug=slug)
		form = PostForm(instance=news)

		context={
		"form":form,
		"Posts":news
		}

		return render(request,self.template, context)
		

	def post(self,request,slug):
		news = get_object_or_404(Posts,slug=slug)
		form = PostForm(request.POST, instance=news)

		if form.is_valid():
			form.save()
			return redirect("index")
		else:
			context = {
				"form":form,
				"Posts":news
			}
			return render(request,self.template, context)


class Delete(View):
	def post(self,request,slug):
		news = get_object_or_404(Posts,slug=slug)
		news.delete()
		return redirect("index")




