


# --- Logout View ---
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('home')
    next_url = request.GET.get('next', '/')
    return render(request, 'registration/logout.html', {'next': next_url})

# --- Signup View ---
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Event, Registration
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .serializers import EventSerializer, RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyRegistrationsView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)

class CancelRegistrationView(generics.DestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        registration = self.get_object()
        if registration.user != request.user:
            return Response({'error': 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        registration.delete()
        return Response({'status': 'Registration cancelled.'}, status=status.HTTP_204_NO_CONTENT)

class EventListView(TemplateView):
    template_name = 'hello/event_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'hello/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        user = self.request.user
        context['user'] = user
        context['registered'] = False
        context['registration_id'] = None
        if user.is_authenticated:
            reg = Registration.objects.filter(user=user, event=event).first()
            if reg:
                context['registered'] = True
                context['registration_id'] = reg.id
        return context

@login_required
def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reg, created = Registration.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', pk=event.pk)

@login_required
def cancel_registration(request, pk):
    reg = get_object_or_404(Registration, pk=pk, user=request.user)
    event_id = reg.event.id
    reg.delete()
    return redirect('event_detail', pk=event_id)

@method_decorator(login_required, name='dispatch')
class MyRegistrationsTemplateView(TemplateView):
    template_name = 'hello/my_registrations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registrations'] = Registration.objects.filter(user=self.request.user)
        return context
