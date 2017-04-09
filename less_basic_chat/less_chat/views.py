from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Room, Message
from .forms import RoomForm, MessageForm

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.updated_at = timezone.now()
            room.save()
            return redirect('root')
    else:
        form = RoomForm()
    return render(request, 'rooms/new.html', {'form': form})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'rooms/detail.html', {'room': room })
