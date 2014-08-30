from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sharecar_hackathon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'userprofile.views.home', name='home'),
    #url(r'^about', 'userprofile.views.about', name='about'),
    url(r'^login','userprofile.views.user_login',name='user_login'),
    url(r'^logout','userprofile.views.user_logout',name='user_logout'),
    url(r'^signup','userprofile.views.signup',name="signup"),
    url(r'^profile','userprofile.views.profile',name="profile"),
    url(r'^addjourney','userprofile.views.addjourney',name="addjourney"),
    url(r'^admin/', include(admin.site.urls)),
)
