from django.shortcuts import get_object_or_404, redirect, render

from .models import *


def home(request):
  
    return render(request, 'app/home.html')
def create_resume(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        domain = request.POST.get('domain')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        linkedin_profile = request.POST.get('linkedin_profile')
        address = request.POST.get('address')
        summary = request.POST.get('summary')
        
        resume = Resume.objects.create(
            first_name=first_name,
            last_name=last_name,
            domain=domain,
            contact=contact,
            email=email,
            linkedin_profile=linkedin_profile,
            address=address,
            summary=summary
        )
        
        return redirect('education_details', resume_id=resume.id)
    else:
        return render(request, 'app/create_resume.html')

def education_details(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        schooling = request.POST.get('schooling')
        schooling_duration = request.POST.get('schooling_duration')
        intermediate = request.POST.get('intermediate')
        intermediate_duration = request.POST.get('intermediate_duration')
        btech = request.POST.get('btech')
        branch = request.POST.get('branch')
        btech_duration = request.POST.get('btech_duration')
        
        Education.objects.create(
            resume=resume,
            schooling=schooling,
            schooling_duration=schooling_duration,
            intermediate=intermediate,
            intermediate_duration=intermediate_duration,
            btech=btech,
            branch=branch,
            btech_duration=btech_duration
        )
        
        return redirect('certificates', resume_id=resume.id)
    else:
        return render(request, 'app/education_form.html')

def certificates(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        certificate_description = request.POST.get('certificates')
        
        Certificate.objects.create(
            resume=resume,
            description=certificate_description
        )
        
        return redirect('languages', resume_id=resume.id)
    else:
        return render(request, 'app/certificates_form.html')

def languages(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        language = request.POST.get('languages')
        
        Language.objects.create(
            resume=resume,
            language=language
        )
        
        return redirect('skills', resume_id=resume.id)
    else:
        return render(request, 'app/languages_form.html')


def skills(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        skill_name = request.POST.get('skills')
        
        if skill_name:
            Skill.objects.create(resume=resume, name=skill_name)
        
        return redirect('work_experience', resume_id=resume.id)
    else:
        return render(request, 'app/skills_form.html')


def work_experience(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        duration = request.POST.get('duration')
        company_name = request.POST.get('company_name')
        position = request.POST.get('position')
        description = request.POST.get('description')
        
        WorkExperience.objects.create(
            resume=resume,
            duration=duration,
            company_name=company_name,
            position=position,
            description=description
        )
        
        return redirect('view_resume', resume_id=resume.id)
    else:
        return render(request, 'app/work_experience_form.html')

def view_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    educations = Education.objects.filter(resume=resume)
    skills = Skill.objects.filter(resume=resume)
    certificates = Certificate.objects.filter(resume=resume)
    languages = Language.objects.filter(resume=resume)
    work_experiences = WorkExperience.objects.filter(resume=resume)
    
    context = {
        'resume': resume,
        'educations': educations,
        'skills': skills,
        'certificates': certificates,
        'languages': languages,
        'work_experiences': work_experiences,
    }
    
    return render(request, 'app/resume.html', context)

def all_resumes(request):
    resumes = Resume.objects.all()
    resume_data = []

    for resume in resumes:
        educations = Education.objects.filter(resume=resume)
        skills = Skill.objects.filter(resume=resume)
        certificates = Certificate.objects.filter(resume=resume)
        languages = Language.objects.filter(resume=resume)
        work_experiences = WorkExperience.objects.filter(resume=resume)
        
        resume_data.append({
            'resume': resume,
            'educations': educations,
            'skills': skills,
            'certificates': certificates,
            'languages': languages,
            'work_experiences': work_experiences,
        })
    
    context = {
        'resume_data': resume_data
    }
    
    return render(request, 'app/all_resume.html', context)


def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        resume.delete()
        return redirect('all_resumes')
    return render(request, 'app/all_resumes.html', {'resume': resume})
