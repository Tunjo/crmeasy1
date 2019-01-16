from django.shortcuts import render
from django.views.generic import ListView
from .models import ItemStorage
from django.http import HttpResponseRedirect
from .form import ItemForm
from django.core.urlresolvers import reverse
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404




class ItemList(ListView):
    model = ItemStorage
    template_name = 'itemstorage/item_storage.html'
    context_object_name = 'itemstorages'


def item_new(request):
    print(request.POST)
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            rederekt_url = reverse('item_list')

            return HttpResponseRedirect(rederekt_url)
    else:
        form = ItemForm()
    variables = {
        'form': form,
        }

    template = 'itemstorage/item_form.html'

    return render(request, template, variables)


def item_update(request, id):
    obj = get_object_or_404(ItemStorage, id=id)
    if request.POST:
        form = ItemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item_list'))
    else:
        print(obj.name)
        print(obj.created_on)
        form = ItemForm(instance=obj)

    context = {
        'form': form
    }

    return render(request, 'itemstorage/item_form.html', context)


class ItemMixin(object):
    model = ItemStorage

    def get_contex_data(self, **kwargs):
        kwargs.update({'object_name': 'Item'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemMixin, self).dispatch(*args, **kwargs)


class ItemDelete(ItemMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

    def get_object(self, queryset=None):
        #item_id = self.request.path.split('/')[2]
        #obj = ItemStorage.objects.get(id=item_id)
        #print(obj)
        print (self.request)
        obj = super(ItemDelete, self).get_object()
        return obj

    def get_success_url(self):
        return reverse('item_list')