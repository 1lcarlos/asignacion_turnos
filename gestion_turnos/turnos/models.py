from django.db import models

# Create your models here.
class Usuario(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True)
    nombre_Completo = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.nombreCompleto} - {self.cedula}"
    
class Tramite(models.Model):
    tramite_id = models.AutoField(primary_key=True)
    nombre_tramite = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_tramite

class Ventanilla(models.Model):
    ventanilla_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Turno(models.Model):
    ESTADO_CHOICES = [
        ('En espera', 'En espera'),
        ('En proceso', 'En proceso'),
        ('Atendido', 'Atendido'),
        ('Cancelado', 'Cancelado'),
    ]
    turno_id = models.AutoField(primary_key=True)
    cedula_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE)
    fecha_hora_asignacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='En espera')
    numero_turno = models.PositiveIntegerField()
    ventanilla = models.ForeignKey(Ventanilla, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Turno {self.numero_turno} - {self.estado}"

   