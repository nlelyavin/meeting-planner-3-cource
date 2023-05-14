from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="main"),

    # Teams
    path('teams/', include([
        path('', views.index, name='teams'),
        path('team', views.index, name='team'),
        path('<int:id>', views.index, name='team_by_id'),
        path('<int:id>/changeMeetingName', views.index, name='change_meeting_name'),
    ])),

    # Profile
    path('profile/', views.index, name='profile'),

    # Meetings
    path('meeting', include([
        path('<int:id>', views.index, name='meeting_by_id'),
        path('delete/${meeting.id}', views.index, name='meeting_delete')
    ])),

]
