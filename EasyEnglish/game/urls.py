from django.urls import path
from . import views

urlpatterns=[
    path('game/',views.game,name='game'),
    path('game/hangman/',views.hangman,name='hangman'),
    path('logout/',views.logout,name='logout'),
    path('get_hangman_by_type/',views.getHangmanByType,name='getHangmanByType'),
]