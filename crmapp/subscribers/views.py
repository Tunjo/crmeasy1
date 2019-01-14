from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import SubscribeForm
from .models import Subscriber
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


def subscribe_new(request, template='subscribes/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            sub = Subscriber(address_one=address_one, address_two=address_two, city=city, state=state, user_rec=user)
            sub.save()

            authenticated = authenticate(username=username, password=password)
            if authenticated is not None:
                if authenticated.is_active:
                    login(request, authenticated)
                    return HttpResponseRedirect(reverse('account_list'))
                else:
                    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))
            else:
                return HttpResponseRedirect(reverse('sub_new'))

    else:
        form = SubscribeForm()

    return render(request, template, {'form': form})






