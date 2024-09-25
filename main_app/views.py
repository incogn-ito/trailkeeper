from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Goal, Milestone
from .forms import StepForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def goal_index(request):
  goals = Goal.objects.all()
  return render(request, 'goals/index.html', { 'goals': goals })

def goal_detail(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    step_form = StepForm()
    return render(request, 'goals/detail.html', { 'goal': goal, 'step_form': step_form })

def add_step(request, goal_id):
  form = StepForm(request.POST)
  if form.is_valid():
    new_step = form.save(commit=False)
    new_step.goal_id = goal_id
    new_step.save()
    return redirect('goal-detail', goal_id=goal_id)

class GoalCreate(CreateView):
  model = Goal
  fields = ['name', 'category', 'target_date', 'description']
  success_url = '/goals/'

class GoalUpdate(UpdateView):
  model = Goal
  fields = ['name', 'category', 'target_date', 'description']

class GoalDelete(DeleteView):
  model = Goal
  success_url = '/goals/'

class MilestoneCreate(CreateView):
  model = Milestone
  fields = '__all__'

class MilestoneList(ListView):
  model = Milestone

class MilestoneDetail(DetailView):
  model = Milestone
