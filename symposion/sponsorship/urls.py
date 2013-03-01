from django.conf.urls.defaults import patterns, url
#from django.views.generic.simple import direct_to_template
#Changes 1.5
from django.views.generic import TemplateView


urlpatterns = patterns("symposion.sponsorship.views",
    #url(r"^$", direct_to_template, {"template": "sponsorship/list.html"}, name="sponsor_list"),
    url(r"^$", TemplateView.as_view(template_name="sponsorship/list.html")),
    url(r"^apply/$", "sponsor_apply", name="sponsor_apply"),
    url(r"^add/$", "sponsor_add", name="sponsor_add"),
    url(r"^(?P<pk>\d+)/$", "sponsor_detail", name="sponsor_detail"),
)
