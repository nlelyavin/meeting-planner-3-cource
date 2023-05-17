from django.urls import path, include

from meeting_planner.views import ProfileView, index, LoginView

urlpatterns = [
    # Default
    path('', ProfileView.as_view(), name="profile"),

    # Auth
    path('login', LoginView.as_view(), name='login'),

    # Teams
    path('teams/', include([
        path('', index, name='teams'),
        path('team', index, name='team'),
        path('<int:id>', index, name='team_by_id'),
        path('<int:id>/changeMeetingName', index, name='change_meeting_name'),
    ])),

    # Profile
    path('profile/', ProfileView.as_view(), name='profile'),

    # Meetings
    path('meeting', include([
        path('<int:id>', index, name='meeting_by_id'),
        path('delete/${meeting.id}', index, name='meeting_delete')
    ])),

]
