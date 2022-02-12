from django.shortcuts import render, redirect

from forms import MessageForm
from web.models import Message


def leave_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web:message_list')
    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'web/leave_message.html', context)


def message_list(request):
    messages = Message.objects.order_by('-create_date')
    context = {'messages': messages}
    return render(request, 'web/message_list.html', context)
