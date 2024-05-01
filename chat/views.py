from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from chat.models import Thread


@login_required
def messages_page(request):

    context = {
        'Threads': threads
    }
  
 return render(request, 'massages.html', context)
