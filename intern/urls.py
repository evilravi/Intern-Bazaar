from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from .models import Post

app_name = 'intern'

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^internship/apply/(?P<pk>[0-9]+)/$', views.apply.as_view(), name='apply'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^base/', views.base, name='base'),
    url(r'^home/', views.home, name='home'),
    url(r'^internship/$', views.internship, name='internship'),
    url(r'^internship/create/$', views.create_internship.as_view(), name='create_internship'),
    url(r'^internship/(?P<pk>[0-9]+)/$', views.ap_detail.as_view(), name='view_internship'),

    url(r'^on_business/$', views.new, name='new'),
    url(r'^on_business/(?P<pk>[0-9]+)/$', views.detail.as_view(), name='detail'),
    url(r'^on_business/(?P<pk>[0-9]+)/delete/$', views.delete_internship.as_view(), name='delete_internship'),
    url(r'^on_business/update/(?P<pk>[0-9]+)$', views.update_internship.as_view(), name='update_internship'),


    url(r'^blog/$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="intern/blog.html"), name= 'blog_list'),

    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model = Post,
                                                         template_name = 'intern/post.html'), name= 'blog_con'),
]
