from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Profile, Mensaje
from .forms import articuloformulario, ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import os
from django.shortcuts import redirect
# Create your views here.
def inicio(request):
    context={
        "products": Product.objects.all()
    }
    return render(request, "AppCoderhouse/Achorao/inicio.html", context)

def about(request):
    return(render(request, "AppCoderhouse/Achorao/about.html"))

def buscar(request):
    tipo_articulo = request.GET.get("tipo_articulo", None)
    
    if tipo_articulo is not None:
        articulos = Product.objects.filter(tipo_articulo=tipo_articulo)
        
        if articulos.exists():
            return render(request, "AppCoderhouse/Achorao/resultados.html", {"articulos": articulos})
        else:
            return HttpResponse("No se encontraron resultados para la búsqueda.")
    else:
        return HttpResponse("Debe agregar un tipo de artículo en la consulta.")

def busqueda_articulo(request):
    return render(request, "AppCoderhouse/Achorao/buscar_articulos.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'AppCoderhouse/registration/Signup.html'
    success_url = reverse_lazy('Inicio')

class Login(LoginView):
    
    next_page = reverse_lazy('Inicio')
    template_name = 'AppCoderhouse/registration/Login.html'

class Logout(LogoutView):
    template_name = 'AppCoderhouse/registration/Logout.html'

class ProductList(ListView):
    model = Product
    template_name = 'AppCoderhouse/Achorao/product_list.html'
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'AppCoderhouse/Achorao/product_detail.html'

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'AppCoderhouse/Achorao/product_form.html'
    success_url = reverse_lazy("product-list")
    fields = ['producto','precio','titulo', 'estado', 'descripcion', 'imagen']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)
    def handle_no_permission(self):
        return render(self.request, "AppCoderhouse/Achorao/not_found.html")
class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'AppCoderhouse/Achorao/product_form.html'
    success_url = reverse_lazy("product-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        product_id = self.kwargs.get('pk')
        return Product.objects.filter(publisher=user_id, id=product_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "AppCoderhouse/Achorao/not_found.html")

class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'AppCoderhouse/Achorao/product_delete.html'
    success_url = reverse_lazy("product-list")

    def test_func(self):
        user_id = self.request.user.id
        product_id = self.kwargs.get('pk')
        return Product.objects.filter(publisher=user_id, id=product_id).exists()

    def handle_no_permission(self):
        return render(self.request, "AppCoderhouse/Achorao/not_found.html")

class ProfileCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("Inicio")
    form_class = ProfileForm 
    template_name = 'AppCoderhouse/Achorao/profile_create.html'

    def test_func(self):
        return Profile.objects.filter().exists()
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        return render(self.request, "AppCoderhouse/Achorao/not_found.html")


class ProfileUpdate(UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy('Inicio')
    fields = ['imagen', 'info']
    template_name = 'AppCoderhouse/Achorao/profile_update.html'
    
    def test_func(self):
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=self.request.user, id = profile_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "AppCoderhouse/Achorao/not_found.html")

class ProfileDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = 'AppCoderhouse/Achorao/profile_detail.html'

    def test_func(self):
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=self.request.user, id = profile_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "AppCoderhouse/Achorao/not_found.html")
    
class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    template_name = 'AppCoderhouse/Achorao/mensaje_form.html'
    success_url = reverse_lazy('Inicio')

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'AppCoderhouse/Achorao/mensaje_list.html'
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()
    def handle_no_permission(self):
        return render(self.request, "AppCoderhouse/Achorao/not_found.html")
class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mensaje-list")
    template_name = 'AppCoderhouse/Achorao/mensaje_delete.html'
    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id, id=mensaje_id).exists()

    def handle_no_permission(self):
        return render(self.request, "AppCoderhouse/Achorao/not_found.html")