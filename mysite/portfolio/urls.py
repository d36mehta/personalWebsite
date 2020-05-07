from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [

    # the name value is called by the {% url %} template tag
    path('', views.homeview, name='home'),
    path('projects/', views.ProjectView.as_view(), name='project'),
    path('experiences/', views.ExperView.as_view(), name='exper'),
    path('blog/', views.BlogView.as_view(), name='blog'),

]