from django.views import generic
from django.http import HttpResponse
from django.template import loader
from .models import TextBubble, Resume, Quotes


# Create your views here.

def homeview(request):
    template = loader.get_template('portfolio/home.html')
    resume = Resume.objects.all()
    quotes = Quotes.objects.all()
    context = {
        'resume': resume, 'quotes': quotes.order_by('-pub_date'),
    }
    return HttpResponse(template.render(context, request))


class ProjectView(generic.ListView):
    model = TextBubble
    template_name = 'portfolio/projects.html'

    def get_queryset(self):
        """
        includes all project types
        """
        return TextBubble.objects.filter(tag__startswith='P').order_by('-pub_date')


class ExperView(generic.ListView):
    model = TextBubble
    template_name = 'portfolio/exper.html'

    def get_queryset(self):
        """
        includes all experiance types
        """
        return TextBubble.objects.filter(tag__startswith='E').order_by('-pub_date')


class BlogView(generic.ListView):
    model = TextBubble
    template_name = 'portfolio/blog.html'

    def get_queryset(self):
        """
        includes all interests types
        """
        return TextBubble.objects.filter(tag__startswith='I').order_by('-pub_date')
