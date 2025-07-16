from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('skills/', views.SkillListCreate.as_view(), name='skills'),
    path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skill-detail'),
    path('projects/', views.ProjectListCreate.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('education/', views.EducationListCreate.as_view(), name='education'),
    path('education/<int:pk>/', views.EducationDetail.as_view(), name='education-detail'),
    path('experience/', views.ExperienceListCreate.as_view(), name='experience'),
    path('experience/<int:pk>/', views.ExperienceDetail.as_view(), name='experience-detail'),
    path('contact/', views.ContactCreate.as_view(), name='contact'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
] 