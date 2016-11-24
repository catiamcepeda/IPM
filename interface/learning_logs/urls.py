"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views

app_name = 'wam'
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),


    # Show all US.
    url(r'^us/$', views.tipo, name='us'),

    # Show all US.
    url(r'^menu/$', views.menu, name='menu'),

    # Show all US.
    url(r'^sobre/$', views.sobre, name='sobre'),

    # Show all US.
    url(r'^sint_rapida/$', views.sint_rapida, name='sint_rapida'),

    #Dummy request
    url(r'^get_concelho/$', views.get_concelho, name='get_concelho'),

    #Dummy request
    url(r'^get_freguesia/$', views.get_freguesia, name='get_freguesia'),

     #Dummy request
    url(r'^get_loc/$', views.get_loc, name='get_loc'),

     #Dummy request
    url(r'^get_opcao/$', views.get_opcao, name='get_opcao'),
    
     #Dummy request
    url(r'^ped_anterior/$', views.ped_anterior, name='ped_anterior'),
    
     #Dummy request
    url(r'^rec_rapida/$', views.rec_rapida, name='rec_rapida'),

         #Dummy request
    url(r'^edit_sint/$', views.edit_sint, name='edit_sint'),
    
         #Dummy request
    url(r'^new_sint/$', views.new_sint, name='new_sint'),
    
         #Dummy request
    url(r'^edit_rec/$', views.edit_rec, name='edit_rec'),

    
         #Dummy request
    url(r'^edit_rec1/$', views.edit_rec1, name='edit_rec1'),

         #Dummy request
    url(r'^us_loc/$', views.tipo_loc, name='us_loc'),

]