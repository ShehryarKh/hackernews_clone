from django.shortcuts import render,redirect
from django.views.generic import View 
from .forms import PostForm
from .models import Posts
from django.shortcuts import get_object_or_404

# Create your views here.
class Index(View):
	template = "index.html"

	def get(self,request):
		posts = Posts.objects.all()
		print(posts)
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
	def get(self,request,slug):
		news = get_object_or_404(Posts,slug=slug)
		news.Delete()
		return redirect("index")




