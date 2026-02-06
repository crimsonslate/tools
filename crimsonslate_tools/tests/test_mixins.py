from django.test import TestCase, RequestFactory
from crimsonslate_tools.views import mixins
from django.views.generic import TemplateView


class HtmxTemplateResponseMixinTestView(
    mixins.HtmxTemplateResponseMixin, TemplateView
):
    template_name = "test.html"


class HtmxTemplateResponseMixinTestCase(TestCase):
    def setUp(self):
        self.view_cls = HtmxTemplateResponseMixinTestView

    def test_render_to_response_htmx_request(self):
        """Fails if :py:attr:`template_name` wasn't updated to :py:attr:`partial_name` on htmx request."""
        headers = {"HX-Request": "true"}
        request = RequestFactory().get("/", headers=headers)
        view = self.view_cls()
        view.setup(request)
        view.render_to_response(context={})
        self.assertEqual("test.html#main", view.template_name)

    def test_render_to_response_boosted_htmx_request(self):
        """Fails if :py:attr:`template_name` was updated to :py:attr:`partial_name` on boosted htmx request."""
        headers = {"HX-Request": "true", "HX-Boosted": "true"}
        request = RequestFactory().get("/", headers=headers)
        view = self.view_cls()
        view.setup(request)
        view.render_to_response(context={})
        self.assertEqual("test.html", view.template_name)

    def test_render_to_response_non_htmx_request(self):
        """Fails if :py:attr:`template_name` was updated to :py:attr:`partial_name` on non-htmx request."""
        headers = {}
        request = RequestFactory().get("/", headers=headers)
        view = self.view_cls()
        view.setup(request)
        view.render_to_response(context={})
        self.assertEqual("test.html", view.template_name)
