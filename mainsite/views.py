from django.shortcuts import render
from django.http import HttpResponse
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
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", locals())	

