from django.conf.urls import url,patterns
from institute import views

urlpatterns = patterns('',
	url(r'^$', views.home, name = 'home'),
	url(r'^department/(?P<dept_code>[\w\-]+)$', views.department, name = 'dept_home'),
	url(r'^department/(?P<dept_code>[\w\-]+)/people/faculty/$',views.faculty,name ='faculty'),
	url(r'^department/(?P<dept_code>[\w\-]+)/people/student/$',views.student,name='student'),
	url(r'^department/(?P<dept_code>[\w\-]+)/people/staff/$',views.staff,name='staff'),
	url(r'^department/(?P<dept_code>[\w\-]+)/course/$',views.course,name='course'),
	url(r'^department/(?P<dept_code>[\w\-]+)/course/btech/$',views.course,name='btech'),
	url(r'^department/(?P<dept_code>[\w\-]+)/course/mtech_idd/$',views.course,name='mtech_idd'),
	url(r'^department/(?P<dept_code>[\w\-]+)/course/phd/$',views.course,name='phd'),
	url(r'^department/(?P<dept_code>[\w\-]+)/research/$',views.research,name='research'),
	url(r'^department/(?P<dept_code>[\w\-]+)/placement/$',views.placement,name='placement'),
	
	url(r'^notification/$',views.notification_all,name = 'index_notific'),
	url(r'^department/(?P<dept_code>[\w\-]+)/notification/$',views.notification_all, name = 'dept_notific'),
    url(r'^notification/(?P<notif_title_slug>[\w\-]+)/$',views.notification,name = 'notification'),
    url(r'^department/(?P<dept_code>[\w\-]+)/notification/(?P<notif_title_slug>[\w\-]+)/$',views.notification, name = 'dept_notific_view'),
	)
