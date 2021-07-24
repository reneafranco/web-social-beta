from django.shortcuts import render, redirect

from .models import Post, Comment, Profile

from .forms import Post_Form, Comment_form, Register_form, Profile_form

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

# Send Mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import time


@login_required(login_url="Index")
def Home(request):
    posts = Post.objects.all().order_by('-created_at')
    test = Profile.objects.all()
    content = {
        'post_list': posts,
        'test':test
    }

    return render(request, 'pages/home.html', content)


@login_required(login_url="Index")
def Add_Post(request):
    posts = Post.objects.all()
    form = Post_Form(request.POST)

    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()

        return redirect('Home')

    content = {
        'post_list': posts,
        'form': form,
    }

    return render(request, 'pages/add_post.html', content)


@login_required(login_url="Index")
def Post_Detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = Comment_form(request.POST)
    comment = Comment.objects.all()

    comments = Comment.objects.filter(post=post).order_by('-created_at')

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.author = request.user
        new_comment.post = post
        new_comment.save()

        return redirect('post-detail', pk=post.pk)

    content = {
        'post': post,
        'form': form,
        'comments': comments,
        'comment': comment,
    }

    return render(request, 'pages/post_detail.html', content)


@login_required(login_url="Index")
def Post_Edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = Post_Form(instance=post)

    content = {
        'post': post,
        'form': form
    }
    if request.method == "POST":
        form = Post_Form(request.POST, instance=post)

        if form.is_valid():
            form.save()

            return redirect('post-detail', pk=post.pk)

    return render(request, 'pages/post_edit.html', content)


@login_required(login_url="Index")
def Post_Delete(request, pk):
    post = Post.objects.get(pk=pk)

    content = {
        'post': post
    }

    if request.method == "POST":
        post.delete()
        return redirect('Home')

    return render(request, 'pages/post_delete.html', content)


@login_required(login_url="Index")
def Comment_Edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    form = Comment_form(instance=comment)

    content = {
        'comment': comment,
        'form': form,
    }

    if request.method == "POST":
        form = Comment_form(request.POST, request.FILES, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.pk)

    return render(request, 'pages/comment_edit.html', content)


@login_required(login_url="Index")
def Comment_Delete(request, pk):
    comment = Comment.objects.get(pk=pk)

    content = {
        'comment': comment
    }

    if request.method == "POST":
        comment.delete()

        return redirect('post-detail', pk=comment.post.pk)

    return render(request, 'pages/comment_delete.html', content)


def Register(request):

    form = Register_form()
    if request.method == "POST":
        form = Register_form(request.POST)
        if form.is_valid():
            form.user = request.user
            user = form.save()
            form.save()


            template = render_to_string('profiles/email.html',
                                        {'name': request.user.username,
                                         'created_at': time.time(),
                                         })
            email = EmailMessage(
                'Thanks for Sing up in Karma',
                template,
                settings.EMAIL_HOST_USER,
                [user.email], )

            email.fail_silently = False
            email.send()

            return redirect('Home')
    content = {
                'register_form': form
            }

    return render(request, 'profiles/register_page.html', content)


@login_required(login_url="Index")
def Profile_View(request, pk):
    profile = Profile.objects.get(pk=pk)
    user = profile.user
    posts = Post.objects.filter(author=user).order_by('-created_at')

    content = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'profiles/profile.html', content)


def login(request):
    if request.user.is_authenticated:
        return redirect('Home')

    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('Home')

            else:
                return redirect('login')

    return render(request, 'profiles/login_page.html')


def logout_page(request):
    logout(request)
    return redirect('Index')


@login_required(login_url="Index")
def Create_Profile(request, pk):
    pk = request.user.pk
    profile = Profile.objects.all()


    form = Profile_form()

    content = {
        'profile': profile,
        'form': form,
    }

    if request.method == "POST":
        form = Profile_form(request.POST)

        if form.is_valid():
            user = form.save()
            user.user = request.user
            user.save()

            return redirect('profile' , pk=user.pk)

    content = {
        'form': form
    }

    return render(request, 'profiles/create_profile.html', content)


def Profile_Edit(request, pk):
    profile = Profile.objects.get(pk=pk)
    form = Profile_form(instance=profile)

    content = {
        'profile': profile,
        'form': form,
    }

    if request.method == "POST":
        form = Profile_form(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('profile', pk=profile.pk)

    return render(request, 'profiles/profile_edit.html', content)