from django.shortcuts import render, redirect, get_object_or_404
from .models import UserModel
from .forms import UserModelForm

def index_view(request):
    users = UserModel.get_all_users()
    return render(request, 'userApp/index.html', {'users': users})

def create_user_view(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_view')
    else:
        form = UserModelForm()

    return render(request, 'userApp/create_user.html', {'form': form})

def delete_user_view(request, pk):
    UserModel.delete_user(pk)
    return redirect('index_view')

def edit_user_view(request, pk):
    user = get_object_or_404(UserModel, pk=pk)

    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index_view')
    else:
        form = UserModelForm(instance=user)

    return render(request, 'userApp/edit_user.html', {'form': form, 'user': user})
