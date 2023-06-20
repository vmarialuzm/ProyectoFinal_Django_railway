from django.shortcuts import render
from formulario.models import Proyecto
from django.views.generic import View

class Index(View):
  def get(self,request):
    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos}
    return render(request,'index.html',context)
  
def portfolio_details(request,id):
    portfolio_details = Proyecto.objects.get(id=id)
    context={"portfolio_details": portfolio_details}
    return render(request,'portfolio-details.html',context)
