from django.urls import path, include

from meeting_planner.views import (
    ProfileView, index, LoginView, RegistrationView, logout_view, TeamsView, TeamView, MeetingView
)

urlpatterns = [

    # Base
    path('', ProfileView.as_view(), name="main"),
    path('login', LoginView.as_view(), name='login'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('logout', logout_view, name='logout'),

    # Teams
    path('teams/', include([
        path('', TeamsView.as_view(), name='teams'),
        path('<int:pk>', TeamView.as_view(), name='team_by_id'),
    ])),

    # Profile
    path('profile/', ProfileView.as_view(), name='profile'),

    # Meetings
    path('meeting/', include([
        path('<int:pk>', MeetingView.as_view(), name='meeting_by_id'),
        path('<int:id>/changeMeetingName', index, name='change_meeting_name'),
        path('<int:id>/delete', index, name='meeting_delete'),
        path('<int:pk>/schedule', index, name='meeting_schedule'),
    ])),

]
