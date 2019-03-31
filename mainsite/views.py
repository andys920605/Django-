from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from mainsite.models import Post
# Create your views here.

#def homepage(request):
#    posts = Post.objects.all()
#    post_lists = list()
#    for count, post in enumerate(posts):
#        post_lists.append("NO.{}:".format(str(count))+str(post.title)+"<hr>")
#        post_lists.append("<small>" +str(post.body)+"</small><br><br>")
#    return HttpResponse(post_lists)


def homepage(request):
    posts = Post.objects.all().order_by('-id')
    
    now = datetime.now()
    return render(request, "index.html", locals())	

def showpost(request,id):
    try:
       
        post = Post.objects.get(id=id)
        if post != None:
            return render(request,"post.html",locals())
    except:
        return redirect('/')    


