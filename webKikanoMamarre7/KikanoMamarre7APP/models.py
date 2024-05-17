from django.db import models

# Modelo de Editorial
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField(max_length=100)

    def _str_(self):
        return self.nombre


# Modelo de Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()

    def _str_(self):
        return self.nombre


# Modelo de Género
class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def _str_(self):
        return self.nombre


# Modelo de Libro
class Libro(models.Model):
    DISPONIBLE = 'disponible'
    PRESTADO = 'prestado'
    RESERVADO = 'reservado'
    ESTADO_CHOICES = [
        (DISPONIBLE, 'Disponible'),
        (PRESTADO, 'Prestado'),
        (RESERVADO, 'Reservado'),
    ]

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    numero_ejemplar = models.IntegerField()
    numero_paginas = models.IntegerField()
    año_publicacion = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def _str_(self):
        return self.titulo


# Modelo de Préstamo
class Prestamo(models.Model):
    ACTIVO = 'activo'
    DEVUELTO = 'devuelto'
    ESTADO_PRESTAMO_CHOICES = [
        (ACTIVO, 'Activo'),
        (DEVUELTO, 'Devuelto'),
    ]

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado_prestamo = models.CharField(max_length=10, choices=ESTADO_PRESTAMO_CHOICES)
    multa = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.libro}"


# Modelo de Reserva
class Reserva(models.Model):
    ACTIVO = 'activo'
    CANCELADO = 'cancelado'
    ESTADO_RESERVA_CHOICES = [
        (ACTIVO, 'Activo'),
        (CANCELADO, 'Cancelado'),
    ]

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    estado_reserva = models.CharField(max_length=10, choices=ESTADO_RESERVA_CHOICES)

    def _str_(self):
        return f"{self.libro}"