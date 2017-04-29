from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HowdyPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'howdyindex.html', context=None)

class AboutHowdyView(TemplateView):
    template_name = "about.html"
