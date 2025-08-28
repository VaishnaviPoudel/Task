DEFAULT_DAILY_GOAL=2000

from django.shortcuts import render, redirect
from .models import WaterIntake, WaterIntakeGoal
from .forms import WaterIntakeForm, WaterIntakeGoalForm, UserRegistrationForm, LoginForm
from datetime import date
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.user.is_authenticated:
        total_intake = todays_intake(request.user)
        daily_goal = get_user_goal(request.user)
        remaining = daily_goal - total_intake if daily_goal > total_intake else 0
        show_welcome = request.session.pop('just_logged_in', False)
        goal_completed = total_intake >= daily_goal


        context = {
            'total_intake': total_intake,
            'daily_goal': daily_goal,
            'remaining': remaining,
            'show_welcome': show_welcome,
            'goal_completed': goal_completed
            
            }
    else:
        context = {
            'total_intake': 0,
            'daily_goal': DEFAULT_DAILY_GOAL,
            'remaining': 0,
            'show_welcome': False,
            'goal_completed': False

        }

    return render(request, 'home.html', context)

def todays_intake(user):
    today = date.today()
    intakes = WaterIntake.objects.filter(user=user, time__date=today)
    
    total = 0
    for intake in intakes:
        total += intake.amount
    
    return total

def get_user_goal(user):
    try:
        return WaterIntakeGoal.objects.get(user=user).daily_goal_amount
    except WaterIntakeGoal.DoesNotExist:
        return DEFAULT_DAILY_GOAL  
    

@login_required
def add_water_intake(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            intake = form.save(commit=False)
            intake.user = request.user
            previous_total = todays_intake(request.user)
            intake.save()
            total = previous_total + intake.amount

            goal = get_user_goal(request.user)
            if previous_total < goal <= total:
                messages.success(request, 'You reached your daily goal!')
            elif total < goal:
                messages.success(request, 'Water intake added successfully!')

            return redirect('home')
    else:
        form = WaterIntakeForm()

    total = todays_intake(request.user)
    goal = get_user_goal(request.user)

    context = {
        'form': form,
        'total': total,
        'goal': goal,
    }
    return render(request, 'add_water_intake.html', context)

@login_required
def update_goal(request):
    try:
        goal_instance = WaterIntakeGoal.objects.get(user=request.user)
    except WaterIntakeGoal.DoesNotExist:
        goal_instance = None

    if request.method == 'POST':
        form = WaterIntakeGoalForm(request.POST, instance=goal_instance)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Daily goal updated successfully!')
            return redirect('home')
    else:
        form = WaterIntakeGoalForm(instance=goal_instance)

    return render(request, 'set_goal.html', {'form': form})




@login_required
def weekly_history(request):
    today = timezone.now().date()
    history = []
    goal = get_user_goal(request.user)

    for i in range(6, -1, -1): 
        day = today - timedelta(days=i)
        intakes = WaterIntake.objects.filter(user=request.user, time__date=day)
        
        total = sum(intake.amount for intake in intakes)

        history.append({
            'date': day,
            'amount': total,
            'met_goal': total >= goal
        })

    context= {
        'history': history, 
        'goal': goal
    }

    return render(request, 'weekly_history.html', context)



def register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('login_page')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['just_logged_in'] = True

                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_page(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')
