from django.shortcuts import render, HttpResponseRedirect, reverse, Http404, HttpResponse
from django.views.generic import TemplateView


class EditView(TemplateView):
    template_name = 'editor/index.html'

