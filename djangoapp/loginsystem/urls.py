from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstpage),
    path('',views.login)
   
]

# #leave




# urlpatterns = [
#     path('leave_request/', views.leave_request, name='leave_request'),
#     path('leave_approve/<int:id>/', views.leave_approve, name='leave_approve'),
#     path('leave_reject/<int:id>/', views.leave_reject, name='leave_reject'),
# ]