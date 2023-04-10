from django.shortcuts import render, redirect


from .forms import RegistrationForm


# Create your views here.

def register(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('shop:product_list')
    else:
        form = RegistrationForm()
    return render(request, template_name='registration/register.html', context={'form': form})
