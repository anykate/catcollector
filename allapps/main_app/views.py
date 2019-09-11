from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat


# Create your views here.
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'


class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
    model = Cat
    # success_url = '/cats/'

    def get_success_url(self):
        return reverse('main_app:index')


def home(request):
    return render(request, 'main_app/home.html')


def about(request):
    return render(request, 'main_app/about.html')


def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'main_app/index.html', {'cats': cats})


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'main_app/detail.html', {'cat': cat})
