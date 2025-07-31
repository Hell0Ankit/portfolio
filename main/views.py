from django.shortcuts import render
from .models import Profile,SocialMedia,Buttons,AboutMe,PersonalDetails,Skills,Expericence,Education,Project

def home(request):
    profile = Profile.objects.first()
    socialicon = SocialMedia.objects.all()
    buttons = Buttons.objects.first()
    about_data = AboutMe.objects.first()
    Personal_Details = PersonalDetails.objects.all()
    my_skill = Skills.objects.all()
    expericence = Expericence.objects.all()
    education = Education.objects.all()
    project = Project.objects.all()

    return render(request, 'portfolio/home.html',
                   {'profile': profile,
                    'socialicon': socialicon,
                    'buttons': buttons,
                    'about_data': about_data,
                    'Personal_Details': Personal_Details,
                    'my_skill': my_skill,
                    'expericence': expericence,
                    'education': education,
                    'project': project,
                    })










