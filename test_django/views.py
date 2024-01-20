from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'
