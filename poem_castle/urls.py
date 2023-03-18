from django.urls import path
from . import views
app_name = 'poem_castle'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('home', views.MainView.as_view(), name='home'),
    path(
        route='collection/<str:slug>',
        view=views.CollectionPoemView.as_view(),
        name='collection'
    ),
    path(
        route='poem/<str:slug>/<int:id>',
        view=views.PoemDetail.as_view(),
        name='poem_detail'
    ),
    path(
        route='all-poems',
        view=views.PoemListView.as_view(),
        name='poem_list'
    ),
    path(
        route='search_results',
        view=views.SearchResultsList.as_view(),
        name='search_results'
    ),
]
