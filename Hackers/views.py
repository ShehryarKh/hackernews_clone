from django.shortcuts import render,redirect
from django.views.generic import View 
from .forms import PostForm,UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Posts
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse


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
	template = "login.html"

	def get(self, request):
		return render(request, self.template, {})

	def post(self, request):
		if request.user.is_authenticated():
			#messages.warning(request, "You are already logged in.")
			return redirect("index")

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return redirect("index")
			else:
				return HttpResponse("your account is disabled.")
		else:
			return HttpResponse("Invalid details")


class Index(View):
	template = "index.html"

	def get(self,request):
		posts = Posts.objects.all().order_by('-created_at')
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

		# post = Posts.objects.get()
		# post = [p.to_jason() for p in post.to_jason()]
		
		if postform.is_valid():
			new_post = postform.save()
			return JsonResponse(new_post.to_json())
		# return JsonResponse({'post':post})


        # postform = PostForm(request.POST)

        # if postform.is_valid():
        #     postform.save()

        #     return redirect("index")
        # else:
        # 	return redirect("index")

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

@login_required
def logout_(request):
	logout(request)

	return redirect('/')



