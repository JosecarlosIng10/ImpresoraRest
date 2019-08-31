from djongo  import models
 
 
class Tool(models.Model):
    label = models.TextField()
    description = models.TextField()