from django.db import models

# Modelo de Editorial

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('bibliotecario', 'Bibliotecario'),
        ('administrador', 'Administrador'),
        ('usuario_regular', 'Usuario Regular'),
    ]

    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.PositiveIntegerField()
    correo_electronico = models.EmailField(max_length=100)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    correo_electronico = models.EmailField()

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    numero_ejemplar = models.IntegerField()
    numero_paginas = models.IntegerField()
    año_publicacion = models.IntegerField()
    estado = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('prestado', 'Prestado'), ('reservado', 'Reservado')])

class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado_prestamo = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('devuelto', 'Devuelto')])
    multa = models.DecimalField(max_digits=10, decimal_places=2)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    estado_reserva = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('cancelado', 'Cancelado')])