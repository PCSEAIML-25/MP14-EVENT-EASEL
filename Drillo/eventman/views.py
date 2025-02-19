from django.shortcuts import render, redirect
from datetime import date
from .forms import FormSubmissionForm
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from user.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages


@login_required
@csrf_exempt
def form_submission(request):
    # Check if user is a coordinator
    if not request.user.is_coordinator:
        messages.error(request, "Only coordinators can create events.")
        return HttpResponseRedirect('/')  # Redirect to home page
    
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            username = request.user
            user = User.objects.get(username=username)
            
            # Append new event to user's events_created
            events_created = user.events_created
            if events_created:
                events_created += " " + form.cleaned_data.get("name")
            else:
                events_created = form.cleaned_data.get("name")
                
            User.objects.filter(username=username).update(events_created=events_created)
            
            submission = form.save(commit=False)
            submission.created_by = request.user  # Add this line if you have a created_by field
            submission.save()
            url = submission.url
            
            messages.success(request, f"Event '{form.cleaned_data.get('name')}' created successfully!")
            return redirect(reverse('page_preview', kwargs={'url': url}))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        user = request.user
        form = FormSubmissionForm()
        
    return render(request, 'create.html', {'form': form, 'email': user.email})

def page_preview(request,url):
    submission = FormSubmission.objects.get(url=url)
    event_name = submission.name
    registered = False
    total_registered = event_details(event_name)['event']['total_registered']
    about = event_details(event_name)['event']['about']
    sponsor = event_details(event_name)['event']['sponsor']
    crousel = event_details(event_name)['event']['crousel']
    if (request.user.is_authenticated and event_name in request.user.events_participated.split()):
        registered = True
    return render(request, 'rendered_page.html', {'submission': submission, 'user': request.user, 'registration_count': total_registered, 'registered': registered, 'other_events': other_events(), 'sponsors': sponsor,"carousel": crousel, "aboutImage": about})

def register(request, event):
    if(request.user.is_authenticated):
        user = User.objects.get(username=request.user)
        events_participated = user.events_participated + \
            " " + event
        User.objects.filter(username=request.user).update(
            events_participated=events_participated)
        return redirect("dashboard")
    else:
        return redirect("login_view")
    
def other_events():
    today_date = date.today()
    events_name = []
    events = FormSubmission.objects.all()
    for event in events:
        if(today_date <= event.end_date):
            events_name.append(event.name)
    return(events_name)


def event_details(event_name):
    total_registered = 0
    event_detail = {'event': {
        'event_name': "",
        'total_registered': 0,
        'created_by': "",
        "start_date": "",
        "end_date": "",
        "sponsor": [], 
        "about": "",
        "crousel": [],
    }, 'user': []}
    users_event_list = User.objects.all().values_list('username', 'events_participated')
    event_info = FormSubmission.objects.get(name=event_name)
    event_detail['event']['event_name'] = event_name
    event_detail['event']['created_by'] = event_info.email
    event_detail['event']['start_date'] = event_info.start_date
    event_detail['event']['end_date'] = event_info.end_date
    event_detail['event']['about'] = event_info.about
    event_detail['event']['sponsor'] = event_info.sponsors.split(",")
    event_detail['event']['crousel'] = event_info.crousel.split(",")
    for user_event in users_event_list:
        single_user_details = {
            'username': "",
            'email': "",
            'branch': "",
            'github': ""
        }
        event_names = user_event[1]
        username = user_event[0]
        event_names.split()
        for event in event_names.split():
            if (event == event_name):
                user = User.objects.get(username=username)
                single_user_details['username'] = username
                single_user_details['email'] = user.email
                single_user_details['branch'] = user.branch
                single_user_details['github'] = user.github
                total_registered += 1
                event_detail['user'].append(single_user_details)
    event_detail['event']['total_registered'] = total_registered
    return(event_detail)

def event_details_page(request, event):
    if(request.user.is_authenticated):
        user = User.objects.get(username=request.user)
        coordinator = user.is_coordinator
        if(coordinator):
            return render(request, 'event_details.html', {'event_details': event_details(event), 'range': range(len(event_details(event)['user'])), 'length': len(event_details(event)['user']), 'user': user})
        else:
            return redirect('dashboard')
    else:
        return redirect('login_view')