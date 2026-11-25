from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Prefetch
from urllib.parse import urlparse


from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here.

def homepage(request):
    
    context = {
        
    }
    return render(request, 'Templates/Main/homepage.html', context)



def courses_select(request, token):
    sel_course = EBooks.objects.filter(token=token).first()
    objectives = sel_course.objectives.split('\n')
    
    publish = []
    resource = Resources.objects.filter(ebooks=sel_course).order_by('-posted_on')
    for r in resource:
        domain = urlparse(r.resource_link).netloc
        domain = domain.removeprefix('www.')
        link = r.resource_link
        domain_dict = {
            'link':link,
            'domain':domain,
        }
        publish.append(domain_dict)
    context = {
        'course':sel_course,
        'objectives':objectives,
        'resource':resource,
        'publisher':publish,
    }
    return render(request, 'Templates/Main/courses_select.html', context)



def courses(request):
    resource = Resources.objects.all().order_by('-posted_on')
    all_courses = EBooks.objects.prefetch_related(Prefetch('resource_books', queryset=resource, to_attr='resource')).order_by('title', '-updated_on', '-posted_on', '-id')
    
    context = {
        'courses':all_courses,
    }
    return render(request, 'Templates/Main/courses.html', context)




def edit(request, token):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        story = request.POST.get('story')
        level = request.POST.get('level')
        category = request.POST.get('category')
        link = request.POST.get('related_links')
        
        parameters_1 = {
            'author':author,
            'title':title,
            'story':story,
            'level':level,
            'category':category,
        }
        
        parameters_2 = {
            'link':link
        }
        
        model = EBooks
        redirect_path = 'courses'
        
        CUD_Functions().edit_content(request, token, model, parameters_1, redirect_path)
    return render(request, 'Templates/Partials/edit_form.html')

    
def delete(request, token):
    if request.method == 'POST':
        model = EBooks
        redirect_path = 'courses'
        
        CUD_Functions().delete_content(request, token, model, redirect_path)
    return render(request, 'Templates/Partials/delete_form.html')

    
    
    
def add(request):
    if request.method == 'POST':
        author = request.POST.get('instructor')
        title = request.POST.get('title')
        story = request.POST.get('story')
        level = request.POST.get('level')
        image = request.POST.get('image_url')
        objectives = request.POST.get('objectives')
        category = request.POST.get('category')
        link = request.POST.get('related_links')
        
        parameters_1 = {
            'author':author,
            'title':title,
            'story':story,
            'level':level,
            'image_url':image,
            'category':category,
            'objectives':objectives,
        }
        checker_1 = {
            'title':title,
        }
        
        model1 = EBooks
        model2 = Resources
        redirect_path = 'courses'
        
        ebook = CUD_Functions().add_content(request, model1, parameters_1, checker_1)
        
        if link:
            parameters_2 = {
                'resource_link':link
            }
            
            checker_2 = {
                'ebooks':ebook,
            }
            
            CUD_Functions().add_content(request, model2, parameters_2, checker_2)
        
        
        return redirect(redirect_path)
    return render(request, 'Templates/Partials/add_form.html')



class CUD_Functions:
    def add_content(self, request, model, parameters, checker):

        ebooks, created = model.objects.update_or_create(**checker, defaults=parameters)
        
        return ebooks
        
        
    
    def delete_content(self, request, token, model, redirect_path):
        ebooks = model.objects.filter(token=token).first()
        
        if ebooks:
            ebooks.delete()
                        
        return redirect(redirect_path)
        
    
    def edit_content(self, request, token, model, parameters, redirect_path):
        ebooks = model.objects.filter(token=token)

        if ebooks:
            edit_ebooks = ebooks.update(**parameters)
                
        return redirect(redirect_path)
        
    



def logout(request):
    auth.logout(request)
    return redirect('/')    


def login_staff(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']

            userauth = auth.authenticate(username=username, password=password)
                                    
            if userauth is not None:
                auth.login(request, userauth)
                return redirect('homepage')
            else:
                messages.error(request, 'Sorry, user does not exist')
                return redirect('staff')
    context = {
        
    }
    return render(request, 'Templates/Main/staff_portal.html', context)
    

def register_staff(request):
    
    context = {
        
    }
    return render(request, 'Templates/Main/staff_portal.html', context)




def community(request):
    
    context = {
        
    }
    return render(request, 'Templates/Main/community.html', context)

def contact_us(request):
    
    context = {
        
    }
    return render(request, 'Templates/Main/contact_us.html', context)

def help_center(request):
    
    context = {
        
    }
    return render(request, 'Templates/Main/help_center.html', context)

def privacy_policy(request):
    
    context = {
        
    }
    return render(request, 'Templates/Main/privacy_policy.html', context)

def terms_n_condition(request):
    
    context = {
        
    }
    return render(request, 'Templates/Main/terms_n_cond.html', context)