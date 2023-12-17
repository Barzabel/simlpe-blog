from django.views.generic.base import TemplateView
from django.shortcuts import (
render
)
from django.template import RequestContext

class IndexPageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context



def page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})