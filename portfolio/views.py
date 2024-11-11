from django.shortcuts import render, get_object_or_404
from .models import Project
from .models import BlogPost
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm



def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'portfolio/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Contact Form Submission',
                'You have received a new message from your portfolio website.',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')
