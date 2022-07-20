from django_request_mapping import UrlPattern
from pig_ham.views import MyView
urlpatterns = UrlPattern();
urlpatterns.register(MyView)
