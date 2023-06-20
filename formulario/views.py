from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Proyecto
from django.views.generic import FormView
from .forms import ProyectoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import cloudinary.uploader

class CreateProyecto(LoginRequiredMixin,FormView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "form.html"

    #Para guardar la informacion existe esta función 
    def form_valid(self, form):
        foto = form.cleaned_data['foto']
        foto_proyecto_details1 = form.cleaned_data['foto_proyecto_details1']
        foto_proyecto_details2 = form.cleaned_data['foto_proyecto_details2']
        foto_proyecto_details3 = form.cleaned_data['foto_proyecto_details3']

        # Subir la imagen a Cloudinary y obtener la URL
        foto_url = cloudinary.uploader.upload(foto)['secure_url']
        foto_proyecto_details1_url = cloudinary.uploader.upload(foto_proyecto_details1)['secure_url']
        foto_proyecto_details2_url = cloudinary.uploader.upload(foto_proyecto_details2)['secure_url']
        foto_proyecto_details3_url = cloudinary.uploader.upload(foto_proyecto_details3)['secure_url']

        # Crear el objeto Proyecto con la URL de la imagen en Cloudinary
        # cleaned_data es el objeto que tiene toda la info que hemos llenado en el formulario
        proyecto = Proyecto(
            foto = foto_url,
            foto_proyecto_details1 = foto_proyecto_details1_url,
            foto_proyecto_details2 = foto_proyecto_details2_url,
            foto_proyecto_details3 = foto_proyecto_details3_url,
            titulo_proyecto = form.cleaned_data['titulo_proyecto'],
            descripcion_proyecto = form.cleaned_data['descripcion_proyecto'],
            tags = form.cleaned_data['tags'],
            url_github = form.cleaned_data['url_github']
            )
        proyecto.save()
        return redirect('index')
    
    def form_invalid(self,form):
        messages.error(self.request,'Por favor, completa todos los campos requeridos')
        return super().form_invalid(form)
        



