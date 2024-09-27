from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Goal, Milestone
from .forms import StepForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def goal_index(request):
  goals = Goal.objects.filter(user=request.user)
  return render(request, 'goals/index.html', { 'goals': goals })

@login_required
def goal_detail(request, goal_id):
  goal = Goal.objects.get(id=goal_id)
  milestones_goal_doesnt_have = Milestone.objects.exclude(id__in = goal.milestones.all().values_list('id'))
  step_form = StepForm()
  return render(request, 'goals/detail.html', {
    'goal': goal, 'step_form': step_form, 'milestones': milestones_goal_doesnt_have
  })

@login_required
def add_step(request, goal_id):
  form = StepForm(request.POST)
  if form.is_valid():
    new_step = form.save(commit=False)
    new_step.goal_id = goal_id
    new_step.save()
    return redirect('goal-detail', goal_id=goal_id)
  
@login_required
def assoc_milestone(request, goal_id, milestone_id):
  Goal.objects.get(id=goal_id).milestones.add(milestone_id)
  return redirect('goal-detail', goal_id=goal_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('goal-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class Home(LoginView):
  template_name = 'home.html'

class GoalCreate(LoginRequiredMixin, CreateView):
  model = Goal
  fields = ['name', 'category', 'target_date', 'description']
  success_url = '/goals/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GoalUpdate(LoginRequiredMixin, UpdateView):
  model = Goal
  fields = ['name', 'category', 'target_date', 'description']

class GoalDelete(LoginRequiredMixin, DeleteView):
  model = Goal
  success_url = '/goals/'

class MilestoneCreate(LoginRequiredMixin, CreateView):
  model = Milestone
  fields = '__all__'

class MilestoneList(LoginRequiredMixin, ListView):
  model = Milestone

class MilestoneDetail(LoginRequiredMixin, DetailView):
  model = Milestone

class MilestoneUpdate(LoginRequiredMixin, UpdateView):
  model = Milestone
  fields = ['name', 'color']

class MilestoneDelete(LoginRequiredMixin, DeleteView):
  model = Milestone
  success_url = '/milestones/'
