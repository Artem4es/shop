from django.shortcuts import redirect, render


from .forms import OrderForm


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # post.save()
            return redirect('https://ya.ru')  # сообщение о удачной отправке!
        return render(request, 'index.html', {'form': form})

    form = OrderForm()
    context = {'form': form}
    return render(request, 'index.html', context)


