
from django.shortcuts import render
from .models import Data
from django.shortcuts import render, redirect
from .models import UserData, JournalEntry
from django.contrib.auth.decorators import login_required 
# Create your views here.


@login_required(login_url="login")
def index(request):
    
    
    
    return render(request,"index.html")

@login_required(login_url="login")
def home(request):
    return render(request,'index.html')

import json
from django.shortcuts import render
from .models import JournalEntry
from collections import Counter


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def profile(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'profile.html', {'user': user})

def dashboard(request):
    if request.user.is_authenticated:
        # Get all journal entries for the logged-in user
        journals = JournalEntry.objects.filter(user=request.user)

        # Count total entries
        count_of_entries = journals.count()

        # Prepare data for the graph
        dates = [journal.timestamp.date() for journal in journals]
        date_counts = Counter(dates)

        # Prepare data for the graph
        graph_dates = list(date_counts.keys())
        graph_counts = list(date_counts.values())
    else:
        count_of_entries = 0
        graph_dates = []
        graph_counts = []

    return render(request, 'dash.html', {
        'count_of_entries': count_of_entries,
        'graph_dates': json.dumps(graph_dates),  # Convert to JSON
        'graph_counts': json.dumps(graph_counts),  # Convert to JSON
    })




def journal(request):
    journals = JournalEntry.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'journal.html', {'journals': journals})

def mindfull(request):
        return render(request, 'mindfulness.html')

def profile(request):
        return render(request, 'profile.html')





import plotly.express as px
from django.shortcuts import render
from .models import JournalEntry

def plot_view(request):
    journals = JournalEntry.objects.all()
    data = [journal.timestamp.date() for journal in journals]
    
    fig = px.histogram(data, x=data, title='Journal Entries Over Time')
    graph = fig.to_html(full_html=False)

    return render(request, 'plot.html', {'graph': graph})

from django.shortcuts import render
from .models import JournalEntry
from collections import Counter
import json

def dashboard(request):
    if request.user.is_authenticated:
        # Get all journal entries for the logged-in user
        journals = JournalEntry.objects.filter(user=request.user)

        # Count total entries
        count_of_entries = journals.count()

        # Prepare data for the graph
        dates = [journal.timestamp.date() for journal in journals]
        date_counts = Counter(dates)

        # Prepare data for the graph
        graph_dates = [date.isoformat() for date in date_counts.keys()]  # Convert date objects to strings
        graph_counts = list(date_counts.values())
    else:
        count_of_entries = 0
        graph_dates = []
        graph_counts = []

    return render(request, 'dash.html', {
        'count_of_entries': count_of_entries,
        'graph_dates': json.dumps(graph_dates),  # Convert to JSON
        'graph_counts': json.dumps(graph_counts),  # Convert to JSON
    })

def add_journal_entry(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        # happiness = request.POST.get('happiness', 3)  # Default to 3 if not provided
        img = request.FILES.get('img')  # File from request.FILES
        audio = request.FILES.get('audio')  # File from request.FILES
        location = request.POST.get('location', '')  # Default to empty string if not provided
        additional = request.FILES.get('additional')  # File from request.FILES

        # Create the journal entry
        JournalEntry.objects.create(
            user=request.user,
            content=content,
            # happiness=happiness,
            img=img,
            audio=audio,
            location=location,
            additional=additional
        )
        return redirect('journal')  # Redirect to dashboard after saving

    return render(request, 'add_journal.html')

def add_journal_entry(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        happiness = request.POST.get('happiness')  # Dropdown valu
        img = request.FILES.get('img')
        audio = request.FILES.get('audio')
        location = request.POST.get('location')
        additional = request.FILES.get('additional')

        # Create a JournalEntry instance
        JournalEntry.objects.create(
            user=request.user,
            content=content,
            happiness=happiness,
            img=img,
            audio=audio,
            location=location,
            additional=additional
        )
        return redirect('/journal')  # Redirect to a success page

    return render(request, 'add_journal.html')