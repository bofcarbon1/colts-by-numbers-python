from django.urls import path
from . import views
from . import views2020

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('factory', views.stats_factory),
    path('team/offense', views.team_offense),
    path('team/defense', views.team_defense),
    path('player/offense', views.player_offense),
    path('player/defense', views.player_defense),
    path('team/offense_2020', views2020.team_offense),
    path('team/defense_2020', views2020.team_defense),
    path('player/offense_2020', views2020.player_offense),
    path('player/defense_2020', views2020.player_defense)
]