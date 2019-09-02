from djongo  import models
 
 
class PrintController(models.Model):
    nombre = models.CharField(max_length=100)
    data = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre