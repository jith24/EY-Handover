# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import date
from django.http import HttpResponse
from .forms import PostForm
from .models import Post, User
# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'feed/post_list.html',{'posts':posts})

def user_list(request):
	day = date.today()
	posts = Post.objects.all().filter(pub=day, shift_choices="D").order_by('published_date')
	return render(request, 'feed/user_list.html',{'posts':posts, 'day':day})


def user_list_date(request):
        date_req = request.POST.get("date")
	if date_req == "":
		date_req=date.today()
	shift = request.POST.get("shift")
	posts = Post.objects.filter(pub=date_req, shift_choices=shift).order_by('published_date')
        return render(request, 'feed/user_list.html',{'posts':posts, 'day':date_req})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'feed/post_detail.html', {'post':post})

def post_file(request, pk):
	post = get_object_or_404(Post, pk=pk)
	filename = post.file.url
	response = HttpResponse(post.file, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	return response

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
	    post.pub = date.today()
            post.save()
            return redirect('feed:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'feed/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
	    post.pub = date.today()
            post.save()
            return redirect('feed:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'feed/post_edit.html', {'form': form})
