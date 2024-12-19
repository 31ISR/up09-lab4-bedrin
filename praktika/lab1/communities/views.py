from django.shortcuts import render, get_object_or_404, redirect
from .models import Community
from django.contrib.auth.decorators import login_required
from . import forms 
from .forms import CommunityCreationForm


def communities_list(req):
    communities = Community.objects.all()  # Получаем все группы из базы данных
    return render(req, 'communities/communities.html', {'communities': communities})


@login_required(login_url="/users/login/")
def create_community(request):
    if request.method == 'POST':
        form = CreateCommunity(request.POST, request.FILES) 
        if form.is_valid():
            new_community = form.save(commit=False)
            new_community.creator = request.user 
            new_community.save()
            return redirect('communities:community_list') 
    else:
        form = CommunityCreationForm()
    return render(request, 'communities/create_community.html', {'form': form})

