from django.views.generic import TemplateView

from . import mixins


class HtmxTemplateView(mixins.HtmxTemplateResponseMixin, TemplateView):
    content_type = "text/html"
    http_method_names = ["get"]
