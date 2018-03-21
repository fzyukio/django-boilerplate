# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    The view to index page
    """
    template_name = 'index.html'