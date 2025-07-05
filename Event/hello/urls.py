
from django.urls import path, include
from hello import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'registrations', views.RegistrationViewSet, basename='registration')

urlpatterns = [
    path("", views.EventListView.as_view(), name="home"),
    path('api/', include(router.urls)),
    path('api/my-registrations/', views.MyRegistrationsView.as_view(), name='my-registrations'),
    path('api/cancel-registration/<int:pk>/', views.CancelRegistrationView.as_view(), name='cancel-registration'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('events/<int:pk>/register/', views.register_event, name='register_event'),
    path('registrations/', views.MyRegistrationsTemplateView.as_view(), name='my_registrations'),
    path('registrations/<int:pk>/cancel/', views.cancel_registration, name='cancel_registration'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]

