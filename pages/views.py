from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


def httpresponse_for_check(request):
    return HttpResponse("reverse done")


def reverse_def(request):
    return HttpResponseRedirect(reverse('httpresponse_for_reverse'))


def reverse_lazy_def(request):
    return HttpResponseRedirect(reverse_lazy('httpresponse_for_reverse'))


class AboutPageView(TemplateView): # new
    template_name = 'about.html'
