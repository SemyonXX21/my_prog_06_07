from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

from .models import Moloko, Yaico, Ourdt
from .forms import LucoshkoForm


def test_view(request):

    return render(request, 'base.html', {})


class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'moloko': Moloko,
        'yaico': Yaico
    }
    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)


    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


def ourdt(request):
    comandaDTs = Ourdt.objects.all()

    return render(request, 'ourdt.html', {'comandaDTs': comandaDTs})

@login_required(login_url= 'login')
def lucoshko(request):
    error = ''
    if request.method == 'POST':
        form = LucoshkoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        else:
            error ='Неверно введено '

    form = LucoshkoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'lucoshko.html', context)