from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import *


# Create your views here.
class Main(TemplateView):
    def post(self, request):
        file = request.FILES.getlist('file')
        print(file)

    #     b = MilModel()
    #     b.header = 'Nidzhat'
    #     b.save()
    #     for i in file:
    #         a = File(file=i)
    #         a.save()
    #         b.key.add(a)
    def get(self, request, *args, **kwargs):
        try:
            del request.session['auth']
        except:
            pass
        a = Voiska.objects.all()
        return render(request, 'index.html', {'a': a})


def calendar(request):
    return render(request, 'calendar.html')


class Vs(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        a = Voiska.objects.get(id=slug)
        b = Voiska1.objects.filter(voiska=slug)
        return render(request, 'vs.html', {'a': a, 'b': b})


class Posts(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        a = Post.objects.filter(voiska=slug)
        b = Voiska1.objects.get(id=slug)
        return render(request, 'posts.html', {'a': a, 'b': b})


class PostDetail(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        a = Post.objects.get(id=slug)
        return render(request, 'post_detail.html', {'a': a})


class Contacts(TemplateView):
    def get(self, request):
        voiska = Voiska.objects.all()
        voiska1 = Voiska1.objects.all()
        ranks = Ranks.objects.all()
        authors = Author.objects.all().order_by('-rank', 'name')
        return render(request, 'contacts.html',
                      {'voiska': voiska, 'voiska1': voiska1, 'authors': authors,'ranks':ranks})
