from .models import Hotel,Bookmark
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SearchForm
from .tasks import scrape_hotels # Celery task for scraping
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
    return redirect('index')

def user_logout(request):
    logout(request)
    return redirect('index')

def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('index')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('index')

        user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('index')

    return redirect('index')

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, "hotels/hotel_list.html", {"hotels": hotels})


def search_hotels(request):
    form = SearchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        scrape_hotels.delay(form.cleaned_data)  # Run the Scrapy spiders asynchronously
        return render(request, 'hotels/loading.html')  # Loading screen while scraping
    return render(request, 'hotels/search.html', {'form': form})



def compare_hotels(request):
    with open('booking.json') as f1, open('agoda.json') as f2:
        booking_hotels = json.load(f1)
        agoda_hotels = json.load(f2)

    results = []
    for bh in booking_hotels:
        for ah in agoda_hotels:
            if bh['hotel_name'].lower() == ah['hotel_name'].lower():
                results.append({
                    'hotel_name': bh['hotel_name'],
                    'booking_price': bh['price'],
                    'agoda_price': ah['price'],
                    'best_price': min(float(bh['price'][4:].replace(',', '')), float(ah['price'][4:].replace(',', ''))),
                    'image': bh['image_url'],
                    'rating': bh['rating'],
                    'booking_url': bh['booking_url'],
                    'agoda_url': ah['booking_url']
                })
    
    return render(request, 'hotels/comparison.html', {'results': results})


@login_required
def bookmark_list(request):
    """Display all bookmarked hotels for the logged-in user."""
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'hotels/bookmark_list.html', {'bookmarks': bookmarks})

@login_required
def bookmark_hotel(request, hotel_id):
    """Allow users to bookmark/unbookmark a hotel."""
    hotel = get_object_or_404(Hotel, id=hotel_id)
    
    # Check if the hotel is already bookmarked
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, hotel=hotel)

    if not created:  # If bookmark already exists, remove it (unbookmark)
        bookmark.delete()
    
    return redirect('bookmarks')  # Redirect back to the bookmarks page