from django.views.generic.base import TemplateResponseMixin


class HtmxTemplateResponseMixin(TemplateResponseMixin):
    """Renders :py:attr:`partial_name` instead of :py:attr:`template_name` when on htmx request."""

    partial_name: str | None = None

    def render_to_response(self, context, **response_kwargs):
        htmx_request = bool(self.request.headers.get("HX-Request"))
        boosted = bool(self.request.headers.get("HX-Boosted"))

        if htmx_request and not boosted:
            if not self.partial_name:
                self.partial_name = f"{self.template_name}#main"
            self.template_name = self.partial_name
        return super().render_to_response(context, **response_kwargs)
