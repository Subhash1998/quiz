from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='quiz_test'

urlpatterns = [
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^about_profile/$',views.about_profile,name='about_profile'),
    url(r'^easy/(?P<test_id>\d+)/$',views.easy,name='easy'),
    url(r'^test_form/$',views.test_form,name='test_form'),
    url(r'^cancel/(?P<test_id>\d+)/$',views.cancel,name='cancel'),
    url(r'^calculate/$',views.calculate_points,name='calculate'),
    url(r'^country/$',views.country,name='country'),
    url(r'change_password/$', views.my_password_change, name='my_password_change'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)