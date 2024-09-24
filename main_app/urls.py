from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('goals/', views.goal_index, name='goal-index'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)