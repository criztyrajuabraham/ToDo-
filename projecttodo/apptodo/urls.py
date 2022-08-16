from django.urls import path

from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvtask/',views.Tasklistview.as_view(),name='cbvtask'),
    path('cbvdetails/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),

]