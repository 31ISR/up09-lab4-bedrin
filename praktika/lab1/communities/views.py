from django.shortcuts import render, get_object_or_404 
from .models import Community

def communities_list(req):
    communities = Community.objects.all()  # Получаем все группы из базы данных
    return render(req, 'communities/communities.html', {'communities': communities})

