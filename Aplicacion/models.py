from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    celular = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    fecha_creada = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	    return self.nombre
    

        
class Especialidad(models.Model):
	CATEGORIA = (
			('A', 'A'),
			('B', 'B'),
			) 

	nombre = models.CharField(max_length=200, null=True)
	precio = models.FloatField(null=True)
	categoria = models.CharField(max_length=200, null=True, choices=CATEGORIA)
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	fecha_creada = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.nombre

class Cita(models.Model):
    ESTADO = (
			('Pendiente', 'Pendiente'),
			('No Asistió', 'No Asistió'),
			('Atendida', 'Atendida'),
			)
    paciente= models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    especialidad= models.ForeignKey(Especialidad, null=True, on_delete=models.SET_NULL)
    fecha_creada = models.DateTimeField(auto_now_add=True, null=True)
    estado = models.CharField(max_length=200, null=True, choices=ESTADO)
    medico= models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.especialidad.nombre