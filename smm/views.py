from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from bot.models import BotUsers, Branch
from django.contrib.auth.decorators import login_required
from .models import Post
from bot.views import bot_request
from .forms import PostForm, PostFormModel1


def smm(request):
    form = PostFormModel1(request.POST or None, request.FILES or None)
    branches = Branch.objects.all()
    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            form.save()

        post = Post.objects.all().last()

        user_id = 394992847
        title = '<b>' + post.post_title + '</b>'
        userModel = BotUsers.objects.all()
        data = form.cleaned_data
        if str(post.image) == 'default.jpg':
            for user in userModel:
                bot_request("sendVideo", {
                                    "chat_id": user.user_id,
                                    'video': 'https://ansorfamily.isaak.uz/media/' + str(post.videofile),
                                    "parse_mode": "html",
                                    # 'video': 'http://ansorfamily.uz/media/videos/' + str(post.videofile),
                                    "caption": title + '\n' + post.post_body
                            })
            return redirect('success')

        else:

            for user in userModel:
                bot_request("sendPhoto", {
                                "chat_id": user.user_id,
                                "parse_mode": "html",
                                'photo': 'https://ansorfamily.isaak.uz/media/' + str(post.image),
                                "caption": title + '\n' + post.post_body
                        })

            return redirect('success')


    return render(request, 'admin_lte/general.html', {"form": form, "branches": branches})


def success(request):
    return render(request, "success.html")
