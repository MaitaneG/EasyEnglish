from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('game/',views.game,name='game'),
    path('game/hangman/',views.hangman,name='hangman'),
    path('game/ranking',views.ranking,name='ranking'),
    path('game/memory_game/',views.memoryGame,name='memory_game'),
    path('game/match_vocabulary/',views.matchVocabulary,name='match_vocabulary'),
    path('logout/',views.logout,name='logout'),
    path('get_hangman_by_type/',views.getHangmanByType,name='getHangmanByType'),
    path('getCards/',views.getCards,name='getCards'),
]

if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)