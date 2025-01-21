from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Course, Profile
from django.contrib.auth.models import User


def home_page(request):
    return render(request, 'courses/home.html', {'user': request.user})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(f'/courses/{user.username}/')
    else:
        form = UserCreationForm()
    return render(request, 'courses/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(f'/courses/{user.username}/')
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'form': form})


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/all_courses.html', {'courses': courses})


def about_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request,'courses/about_course.html', {'course': course})


@login_required
def course_page(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request,'courses/course_page.html', {'course': course})


@login_required
def user_logout(request):
    logout(request)
    return redirect('all_courses')


@login_required
def user_courses(request, username):
    if request.user.username != username:
        return redirect('all_courses')

    user = get_object_or_404(User, username=username)
    user_courses = user.courses.all()

    return render(request, 'courses/user_courses.html', {'courses': user_courses})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    return render(request, 'courses/profile.html', {'user': user, 'profile': profile})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@login_required
def start_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if course not in user.courses.all():
            user.courses.add(course)
        return redirect('course_page', course_id=course.id)
    else:
        return render(request, 'courses/for_login.html')
