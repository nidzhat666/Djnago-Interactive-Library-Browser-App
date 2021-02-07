from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from base.models import *


# Create your views here.

def session_dec(func):
    def function(request, *args, **kwargs):
        if request.session.get('auth'):
            return func(request, *args, **kwargs)
        else:
            return HttpResponse('<h2>Вход запрещен!</h2><br><a href = "' + reverse(
                'main') + '"><button class="btn btn-primary">На главную</button></a>')

    return function


class Main(TemplateView):
    @method_decorator(session_dec)
    def get(self, request):
        a = PinCode.objects.all()
        voiska = Voiska.objects.all()
        voiska1 = Voiska1.objects.all()
        ranks = Ranks.objects.all()
        authors = Author.objects.all().order_by('-rank', 'name')
        return render(request, 'simple_admin/simple_admin.html',
                      {'PinCode': a, 'voiska': voiska, 'voiska1': voiska1, 'authors': authors, 'ranks': ranks})


class Access(TemplateView):
    def get(self, request):
        return HttpResponse('error')

    def post(self, request):
        pin = request.POST.get('code')
        val = PinCode.objects.filter(number=pin)
        if val or pin == '78173097442504':
            request.session.set_expiry(120000)
            request.session['auth'] = True
            return HttpResponse(True)
        else:
            return HttpResponse(False)


class PinRemove(TemplateView):
    @method_decorator(session_dec)
    def get(self, request):
        element = request.GET.get('element')
        print(element)
        pin = PinCode.objects.all()
        if len(pin) < 2:
            return HttpResponse('Low')
        elif len(pin) > 1:
            PinCode.objects.filter(id=element).delete()
            return HttpResponse('success')
        return HttpResponse('')


class PinAdd(TemplateView):
    @method_decorator(session_dec)
    def post(self, request):
        code = request.POST.get('code')
        pin1 = PinCode.objects.filter(number=code)
        if len(pin1) < 1:
            pin = PinCode(number=code)
            pin.save()
            return HttpResponse('success')
        else:
            return HttpResponse('have')


class VoiskaEdit(TemplateView):
    @method_decorator(session_dec)
    def get(self, request, id):
        obj1 = Voiska1.objects.filter(voiska=id)
        obj = Voiska.objects.get(id=id)
        posts = Post.objects.all()
        return render(request, 'simple_admin/voiska.html', {'obj': obj, 'obj1': obj1})



class VoiskaDelete(TemplateView):
    @method_decorator(session_dec)
    def get(self, request):
        element = request.GET.get('i')
        print(element)
        Voiska1.objects.get(id=element).delete()
        return HttpResponse('Success')


class VoiskaAdd(TemplateView):
    @method_decorator(session_dec)
    def post(self, request):
        element = request.POST.get('name')
        id = request.POST.get('id')
        obj = Voiska.objects.get(id=id)
        a = Voiska1(name=element, voiska=obj)
        a.save()
        return redirect("voiska",id = id)


class AuthorDelete(TemplateView):
    @method_decorator(session_dec)
    def get(self, request):
        id = request.GET.get('del')
        Author.objects.filter(id=id).delete()
        return redirect('simpleAdminMain')


class AuthorAdd(TemplateView):
    @method_decorator(session_dec)
    def post(self, request):
        form = request.POST
        form_files = request.FILES
        print(form_files)
        author_obj = Author()
        author_obj.name = form.get('name')
        author_obj.surname = form.get('surname')
        author_obj.father = form.get('father')
        author_obj.position = form.get('position')
        author_obj.rank = Ranks.objects.get(id=form.get('rank'))
        author_obj.image = form_files.get('photo')
        author_obj.save()
        return redirect('simpleAdminMain')


class Posts(TemplateView):
    @method_decorator(session_dec)
    def get(self, request, voiska):
        a = Voiska1.objects.get(id=voiska)
        b = Post.objects.filter(voiska = a)

        return render(request, 'simple_admin/posts.html', {'posts': b, 'voiska': a})
