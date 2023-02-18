from django.shortcuts import render


from main_page.forms import OrderForm
from .telegram import bot, admin_id


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            bike = form.cleaned_data.get('bike')
            phone = form.cleaned_data.get('phone')
            comment =form.cleaned_data.get('comment')

            bot.send_message(chat_id=admin_id, text=f'Ура, новая заявка от {name}!')
            bot.send_message(chat_id=admin_id, text=f'Хочет прошить мотоцикл: {bike}')
            bot.send_message(chat_id=admin_id, text=phone)
            if comment:
                bot.send_message(chat_id=admin_id, text=comment)
            return render(request, 'suc.html')
        return render(request, 'error.html', {'form': form})

    form = OrderForm()
    context = {'form': form}
    return render(request, 'index.html', context)

def yandex_webmaster(request):
    return render(request, 'yandex_551046113a1adf80.html')


