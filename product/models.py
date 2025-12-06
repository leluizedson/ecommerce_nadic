from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(blank=False)

    def __str__(self):
        return self.name
    
class ImageProduct(models.Model):
    ## Pra evitar apagar o banco já existente e dar conflito com novos produtos, pra adicionar imagens
    ## a um produto a gente criou uma nova tabela que relaciona cada imagem a um FK do produto 
    ## correspondente
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"