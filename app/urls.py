from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('create_resume/', views.create_resume, name='create_resume'),
    path('education_details/<int:resume_id>/', views.education_details, name='education_details'),
    path('certificates/<int:resume_id>/', views.certificates, name='certificates'),
    path('languages/<int:resume_id>/', views.languages, name='languages'),
    path('skills/<int:resume_id>/', views.skills, name='skills'),
    path('work_experience/<int:resume_id>/', views.work_experience, name='work_experience'),
    path('resume/<int:resume_id>/', views.view_resume, name='view_resume'),
    path('all_resumes/', views.all_resumes, name='all_resumes'),  # New URL pattern for viewing all resumes
    path('resume/<int:resume_id>/delete/', views.delete_resume, name='delete_resume'),


 
    # Add other URL patterns as needed
]