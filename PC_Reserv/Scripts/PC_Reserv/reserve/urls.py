from django.conf.urls import url, include
from reserve import views
from django.views.generic import TemplateView

app_name = "reserve"

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^hello', views.hello, name='hello'),
    url(r'^book', views.book, name='book'),
    url(r'^book/([0-9]{2})', views.book2, name='book2'),
]
