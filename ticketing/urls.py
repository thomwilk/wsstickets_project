from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.submit_ticket, name='index'),
    path('view/', views.view_tickets, name='view_tickets'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('modify/<int:ticket_id>/<str:new_status>/', views.change_status, name='change_status'),
    path('all/', views.all_tickets, name='all_tickets'),
    path('reply/', views.reply_ticket, name='reply_ticket'),
    path('submitReply/', views.submit_reply, name='submit_reply'),
    path('deletealltickets/', views.delete_all_tickets, name='delete_all_tickets'),
    path('captcha/', include('captcha.urls')),
]




