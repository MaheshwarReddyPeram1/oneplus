from django.contrib import admin
from django.urls import path,include
from onemoreapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
admin.site.site_header = 'jvt connect admin'
admin.site.site_title = 'jvt connect admin'
admin.site.index_title = 'jvt connect adminstration'

urlpatterns = [
    # path('show',views.show, name = 'show'),
    path('',include('account.urls')),
    # path('signin',views.signin, name = 'signin'),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # path('signup',views.signup, name = 'signup'),
    # path('',views.signout, name = 'logout'),
    path('viewreport',views.viewreport, name = 'viewreport'),
    path('viewreport/user',views.viewreport1, name = 'viewreport'),
    path('home',views.home, name = 'home'),
    path('onetoone', views.one2one, name = 'onetoone'),
    path('weeklypresentation', views.weeklypre, name = 'weeklypresentation'),
    path('dailypresentation', views.dailypre, name = 'dailypresentation'),
    path('socials', views.social, name = 'socials'),
    path('visitors', views.visitor, name = 'visitors'),
    path('referralsgiven', views.given, name = 'referralsgiven'),
    path('referralstaken', views.taken, name = 'referralstaken'),
    path('thankyou', views.thankyou, name = 'thankyou'),
    path('jobrecommendation', views.jobrecommendation, name = 'jobrecommendation'),
    path('contactsphere', views.contactsphere, name = 'contactsphere'),
    path('training', views.training, name = 'training'),
    path('mockinterview', views.mockinterview, name = 'mockinterview'),
    path('invite', views.invite, name = 'invite'),
    path('profile',views.profile, name = 'profile'),
    path('edit',views.edit, name = 'edit'),
    # path('onetooneview',views.onetooneview, name = 'onetooneview'),
    # path('dailyview',views.dailyview, name = 'dailyview'),
    # path('weeklyview',views.weeklyview, name = 'weeklyview'),
    # path('socialsview',views.socialsview, name = 'socialsview'),
    # path('visitorsview',views.visitorsview, name = 'visitorsview'),
    # path('referralsgivenview',views.referralsgivenview, name = 'referralsgivenview'),
    # path('referralstakenview',views.referralstakenview, name = 'referralstakenview'),
    path('adminpage',views.adminpage, name = 'adminpage'),
    path('forgotpassword',views.forgotpassword, name = 'forgotpassword'),
    path('needhelp',views.needhelp, name = 'needhelp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)