from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('home/',views.home,name='home'),
   path('', views.projecthome, name='projecthome'),
   path('login/', views.login, name='login'),
   path('login1/', views.login1, name='login1'),
   path('logout/', views.logout, name='logout'),
   path('signup/', views.signup, name='signup'),
   path('signup1/', views.signup1, name='signup1'),
   path('addproducts/',views.addproducts,name='addproducts'),
   path('diningtables/', views.diningtables, name='diningtables'),
   path('feedback/', views.feedback, name='feedback'),
   path('feedback1/', views.feedback1, name='feedback1'),
   path('thank_you/', views.thank_you, name='thank_you'),
   path('study/', views.study, name='study'),
   path('lamp/', views.lamp, name='lamp'),
   path('wooden/', views.wooden, name='wooden'),
   path('lounge/', views.lounge, name='lounge'),
   path('office/', views.office, name='office'),
   path('lhs/', views.lhs, name='lhs'),
   path('sofa3/', views.sofa3, name='sofa3'),
   path('sofa2/', views.sofa2, name='sofa2'),
   path('serveware/', views.serveware, name='serveware'),
   path('knives/', views.knives, name='knives'),
   path('officetable/', views.officetable, name='officetable'),
   path('computertable/', views.computertable, name='computertable'),
   path('door2/', views.door2, name='door2'),
   path('door3/', views.door3, name='door3'),
   path('door4/', views.door4, name='door4'),
   path('ceiling/', views.ceiling, name='ceiling'),
   path('outdoor/', views.outdoor, name='outdoor'),
   path('single/', views.single, name='single'),
   path('double/', views.double, name='double'),
   path('bunk/', views.bunk, name='bunk'),
   path('lounge9/', views.lounge9, name='lounge9'),
   path('buynow/', views.buynow, name='buynow'),
   path('pay/', views.pay, name='pay'),
   path('cart/', views.cart, name='cart'),
   path('credit/', views.credit, name='credit'),
   path('sellerhome/', views.sellerhome, name='sellerhome'),
   path('add_details/', views.add_details, name='add_details'),
   path('view_seller_products/', views.view_seller_products, name='view_seller_products'),
   path('newproducts/', views.newproducts, name='newproducts'),

   #path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)