from django.conf.urls import url
from controlcenter import views

urlpatterns = [
    url(r'^$', views.controlcenter_view, name='control_view'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^change_user_status/$', views.change_status, name='change_status_endpoint'),
    url(r'^users/$', views.users, name='users_endpoint'),

    url(r'^status_api/$', views.status_change_api, name='status_change_api'),
]
