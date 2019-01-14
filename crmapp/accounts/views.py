from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from .models import Account
from .forms import AccountForm
from crmapp.contacts.models import Contact
from crmapp.communications.models import Communication
from crmapp.communications.forms import CommunicationForm

from django.conf import settings


class AccountList(ListView):
    model = Account
    paginate_by = 5
    template_name = 'accounts/accounts_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        try:
            a = self.request.GET.get('account', )
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(name__icontains=a, owner=self.request.user)
        else:
            pass
            account_list = Account.objects.filter(owner=self.request.user)
        return account_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)



@login_required()
def account_detail(request, uuid):
    print(settings.ENV_ROLE)
    if len(uuid) != 22:
        account = Account.objects.get(id=uuid)
        if account.owner != request.user:
            return HttpResponseForbidden()
    else:
        account = Account.objects.get(uuid=uuid)
        if account.owner != request.user:
            return HttpResponseForbidden()

    contacts = Contact.objects.filter(account=account)
    communications = Communication.objects.filter(account=account).order_by('-created_on')
    form = CommunicationForm()

    variables = {
        'account': account,
        'contacts': contacts,
        'communications': communications,
        'form': form,
    }

    return render(request, 'accounts/account_detail.html', variables)


@login_required()
def account_cru(request, uuid=None):

    if uuid:
        account = get_object_or_404(Account, uuid=uuid)
        if account.owner != request.user:
            return HttpResponseForbidden
    else:
        account = Account(owner=request.user)


    if request.POST:
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            redirect_url = reverse(
                'crmapp.accounts.views.account_detail',
                args=(account.uuid, )
            )

            return HttpResponseRedirect(redirect_url)
    else:
        form = AccountForm(instance=account)


    variables = {
        'form': form,
        'account': account
    }

    print(request.is_ajax())
    print(account.name)

    if request.is_ajax():
        template = 'accounts/account_item_form.html'
    else:
        template = 'accounts/account_cru.html'


    return render(request, template, variables)


