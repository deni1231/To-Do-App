from django.conf.urls import url
from django.contrib import admin
from main import views
from django.urls import path

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  path('add_todo/' , views.add_todo),
  path('delete_todo/<int:todo_id>/' , views.delete_todo),
]
