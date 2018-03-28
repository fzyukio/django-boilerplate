# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView

from helloworld.models import Document


class IndexView(TemplateView):
    """
    The view to index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['name'] = 'Yukio'

        txt_documents = Document.objects.filter(type__iexact='txt')

        context['files'] = txt_documents

        return context
