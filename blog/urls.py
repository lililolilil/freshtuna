from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
	url('^', include('django.contrib.auth.urls')),
	url(r'^$', views.home, name='home'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), 
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/list/$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^summernote/', include('django_summernote.urls')),
	#url(r'^accounts/', include('django.contrib.auth.urls')), 
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$',views.signin, name='login'), 
	
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ^login/$ [name='login']
# ^logout/$ [name='logout']
# ^password_change/$ [name='password_change']
# ^password_change/done/$ [name='password_change_done']
# ^password_reset/$ [name='password_reset']
# ^password_reset/done/$ [name='password_reset_done']
# ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^reset/done/$ [name='password_reset_complete']