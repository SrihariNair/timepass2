from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from users.models import CustomUser,  userPosts
from users.forms import PostForm


def birthdaylist(request):
    users=CustomUser.objects.order_by('birth_date')[:]
    context={
    'users':users
    }
    if (request.user.is_authenticated):
        return render(request,'dashboard/birthdaylist.html',context=context)
    else:
        return redirect('home')


def profileview(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request,'dashboard/profileview.html',context=context)


def home(request):
    if(request.user.is_authenticated):
        return render(request,'dashboard/home.html')
    else:
        return redirect('login')


def approval(request):
    leaves = request.user.userposts_set.all().order_by('-created_date')
  #  leaves = userPosts.objects.all().order_by('-created_date')
    context = {
        'leaves': leaves,
    }
    if (request.user.is_authenticated):
        return render(request, 'approval.html', context=context)
    else:
        return redirect('home')



'''class applyleave(generic.CreateView):

    form_class = PostForm
    template_name = 'applyleave.html'
    success_url = reverse_lazy('dashboard:approval')'''

def applyleave(request):
    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard:approval')
    else:
        form = PostForm()
        return render(request, 'applyleave.html', {'form': form})


