from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.forms import UserCreationForm, UserChangeForm, UserAdmin


def user_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Hi', user=request.user.get_email_field_name())
    else:
        form = UserCreationForm()
        return render(request, 'UserCreationForm.html', {'form': form})


def admin_view(request):
    pass
