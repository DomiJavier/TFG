from django.db import models

# MODELOS
class Evento(models.Model):
    title = models.CharField(max_length=50)
    start = models.CharField(max_length=10, primary_key=True)
    lugar = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    def __str__(self):
        return self.title
