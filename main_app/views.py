from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Goal:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, category, creature_type, target_date, description):
    self.name = name
    self.category = category
    self.creature_type = creature_type
    self.target_date = target_date
    self.description = description

goals = [
    Goal("Save $1,000", "Financial", "Squirrel", "2024-12-31", "Save $1,000 by the end of the year for an emergency fund."),
    Goal("Complete a Marathon", "Fitness", "Fox", "2024-10-15", "Train consistently and complete the marathon in October."),
    Goal("Learn French", "Personal Development", "Owl", "2025-06-01", "Become conversational in French by taking weekly lessons and practicing daily."),
    Goal("Launch a Productivity App", "Productivity", "Beaver", "2024-09-30", "Complete and launch a productivity app to help users manage their tasks efficiently.")
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Trailkeepers</h1>')

def about(request):
  return render(request, 'about.html')

def goal_index(request):
  return render(request, 'goals/index.html', { 'goals': goals })