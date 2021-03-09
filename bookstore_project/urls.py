from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    # django-admin
    path('admin/', admin.site.urls),
    #
    # # user management
    # path('accounts/', include('django.contrib.auth.urls')),
    #
    # #Local Apps
    # path('accounts/', include('users.urls')),  # new

    # User management
    path('accounts/', include('allauth.urls')),  # new

    path('', include('pages.urls')), # new
]
