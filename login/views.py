# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login/index.html', context=None)

class LoginView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login/loginpage.html', context=None)

class AboutUsView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login/aboutus.html', context=None)
