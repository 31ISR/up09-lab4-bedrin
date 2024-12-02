from django.shortcuts import render

def posts_list(req):
    return render(req, 'communities/communities.html')
# Create your views here.
