from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('notes/', views.NoteView.as_view()),
    path('notes/<int:pk>', views.SingleNoteView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/', views.Manager.as_view(), name='manager'),
]