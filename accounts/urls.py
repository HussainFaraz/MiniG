from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.introcric,name='introcric'),
    path('IntroRPS/', views.introRPS,name='introRPS'),
    path('Registeration/', views.register,name='registeration'),
    path('Login/', views.login,name='Login'),
    path('Home/',views.user,name='home'),

    #cricket
    path('cricket/', views.toss,name='cricket'),
    path('batting/', views.battingprofile,name='batting'), 
    path('balling/', views.ballingprofile,name='balling'),
    path('battingstart/', views.battingstart,name='battingstart'),   #playerbat first
    path('battingsecond/', views.battingsecond,name='battingsecond'),   #playerbat second
    path('ballingstart/', views.ballingstart,name='ballingstart'),    #opp bat first
    path('ballingsecond/', views.ballingsecond,name='ballingsecond'),    #opp bat second

    #Stone Paper Scissor
    path('RPS/', views.RPS,name='RPS'), 
]