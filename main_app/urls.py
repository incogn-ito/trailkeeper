from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('goals/', views.goal_index, name='goal-index'),
  path('goals/<int:goal_id>/', views.goal_detail, name='goal-detail'),
  path('goals/create/', views.GoalCreate.as_view(), name='goal-create'),
  path('goals/<int:pk>/update/', views.GoalUpdate.as_view(), name='goal-update'),
  path('goals/<int:pk>/delete/', views.GoalDelete.as_view(), name='goal-delete'),
  path('goals/<int:goal_id>/add-step/', views.add_step, name='add-step'),
  path('goals/<int:goal_id>/assoc-milestone/<int:milestone_id>/', views.assoc_milestone, name='assoc-milestone'),
  path('accounts/signup/', views.signup, name='signup'),
  path('milestones/create/', views.MilestoneCreate.as_view(), name='milestone-create'),
  path('milestones/<int:pk>/', views.MilestoneDetail.as_view(), name='milestone-detail'),
  path('milestones/', views.MilestoneList.as_view(), name='milestone-index'),
  path('milestones/<int:pk>/update/', views.MilestoneUpdate.as_view(), name='milestone-update'),
  path('milestones/<int:pk>/delete/', views.MilestoneDelete.as_view(), name='milestone-delete'),
]

# Future ICEBOX - Add code for image upload here.
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)