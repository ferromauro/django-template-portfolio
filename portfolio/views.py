from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from portfolio.models import Project


class PortfolioList(ListView):
    model = Project
    template_name = 'portfolio_list.html'


class PortfolioDetail(DetailView):
    model = Project
    template_name = 'portfolio_detail.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class ContactPage(TemplateView):
    template_name = 'contact.html'