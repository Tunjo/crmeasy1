
from django.http import HttpResponseForbidden
from django.views.generic import ListView
from .models import Blog
from .forms import BlogForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class BlogList(ListView):

    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog'


def user_list_blog(request, id):
    blog_list = Blog.objects.filter(blogger__id=id)
    template = 'blog/user_list_blog.html'

    return render(request, template, {'blog': blog_list})


def blog_new(request):

    if request.POST:
        blog = Blog(blogger=request.user)

        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            redirect_url = reverse('blog_list')

            return HttpResponseRedirect(redirect_url)
    else:
        form = BlogForm
    variables = {
        'form': form,
        }

    template = 'blog/blog_form.html'

    return render(request, template, variables)


def blog_update(request, id):
    if id:
        blog_er = Blog.objects.get(id=id)
    if blog_er.blogger != request.user:
        return HttpResponseForbidden()
    if request.POST:
        form = BlogForm(request.POST, instance=blog_er)

        if form.is_valid():
            form.save()
            HttpResponseRedirect(reverse('blog_list'))

    form = BlogForm(instance=blog_er)

    context = {
        'form': form
    }

    return render(request, 'blog/blog_form.html', context)


class BlogMixin(object):
    model = Blog

    def get_contex_data(self, **kwargs):
        kwargs.update({'object_name': 'item'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BlogMixin, self).dispatch(*args, **kwargs)


class BlogDelete(BlogMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

    def get_object(self, queryset=None):
        print (self.request)
        obj = super(BlogDelete, self).get_object()
        return obj

    def get_success_url(self):
        return reverse('blog_list')
