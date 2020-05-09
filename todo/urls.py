from django.urls import path

from . import views
# independent todo list of app
urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addTodo,name='add'),
    path('complete/<todo_id>',views.completeTodo,name='complete'),
    path('deletecomplete',views.deleteCompleted,name='deletecomplete')
]