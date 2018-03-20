# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from ...core.utils import json_response
from ..models import Comment
from .models import CommentLike
from .forms import LikeForm
@login_required
def update(request, comment_id, five_stars):
        
    comment = get_object_or_404(Comment.objects.exclude(user=request.user), pk=comment_id)
    print(request.method)
    
    if request.method == 'GET':
        form = LikeForm(user=request.user, comment=comment, five_stars=five_stars, data=request.POST)

        if form.is_valid():
            print("The form is valid")            
        else:
            print (form.errors)
 
		#if commentlike exists - update the five_stars value
        try:
            if CommentLike.objects.get(user=request.user, comment=comment) is not None:
                print("CommentLike.objects is not None")
                like = CommentLike.objects.get(user=request.user, comment=comment)
                like.five_stars = five_stars
                like.save()
                
		#if else create a new object                 
        except CommentLike.DoesNotExist:
            print("We create a new object")
            like = form.save()
            like.comment.increase_likes_count()			
			
        if request.is_ajax():
            print("The request is ajax")

        return redirect(request.POST.get('next', comment.get_absolute_url()))
        

    else:
    #    form = LikeForm()
         return redirect(request.POST.get('next', comment.get_absolute_url()))

    context = {
        'form': form,
        'comment': comment
    }

    return render(request, 'spirit/comment/like/create.html', context)

@login_required
def update(request, comment_id, five_stars):
    
    print("FIVE STARS: " + str(five_stars))	
        
    comment = get_object_or_404(Comment.objects.exclude(user=request.user), pk=comment_id)
    print("request.method: " + str(request.method))
#    if request.method == 'POST':
    if request.method == 'GET':
        form = LikeForm(user=request.user, comment=comment, five_stars=five_stars, data=request.POST)

        if form.is_valid():
			#if commentlike exists - update the five_stars value
            try:
                if CommentLike.objects.get(user=request.user, comment=comment) is not None:
                    like = CommentLike.objects.get(user=request.user, comment=comment)
                    like.five_stars = five_stars
                    like.save()
                
			#if else create a new object                 
            except CommentLike.DoesNotExist:
                like = form.save()
                like.comment.increase_likes_count()			
			
            #if request.is_ajax():
            #    print("AJAX")
                
            #    return json_response({'url_delete': like.get_delete_url(), })
    else:
        form = LikeForm()

    context = {
        'form': form,
        'comment': comment
    }

    return redirect(request.POST.get('next', comment.get_absolute_url()))
    #return render(request, 'spirit/comment/like/create.html', context)
