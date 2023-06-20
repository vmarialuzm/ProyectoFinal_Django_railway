from django.db import models
from cloudinary.models import CloudinaryField

class Proyecto(models.Model):
    foto = CloudinaryField('foto')
    foto_proyecto_details1 = CloudinaryField('foto_proyecto_details1')
    foto_proyecto_details2 = CloudinaryField('foto_proyecto_details2')
    foto_proyecto_details3 = CloudinaryField('foto_proyecto_details3')
    titulo_proyecto = models.CharField(max_length=200) 
    descripcion_proyecto = models.TextField()
    tags = models.CharField(max_length=200)
    url_github = models.URLField()

    class Meta:
        db_table = "proyecto"


