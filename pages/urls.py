from django.urls import path
from .views import HomePageView, httpresponse_for_check, reverse_def, reverse_lazy_def, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('httpresponse_for_check', httpresponse_for_check, name='httpresponse_for_reverse'),
    path('reverse_def', reverse_def, name='reverse_it'),
    path('reverse_lazy_def', reverse_lazy_def, name='reverse_lazy_it')
]
