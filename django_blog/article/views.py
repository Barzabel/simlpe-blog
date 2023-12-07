from django.views.generic.base import TemplateView


class ArticlesPageView(TemplateView):

    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = ['one text', 'two text', 'three text']
        return context
