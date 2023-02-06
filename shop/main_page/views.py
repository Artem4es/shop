from django.shortcuts import redirect, render


from main_page.forms import OrderForm


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            form.save()
            # post.save()
            return render(request, 'suc.html')
        return render(request, 'error.html', {'form': form})

    form = OrderForm()
    context = {'form': form}
    return render(request, 'index.html', context)


