from django.db import models

# Create your models here.

class produit (models.Model):
    nom=models.CharField(max_length=500)
    desc=models.TextField()
    prix=models.IntegerField()
    a_prix=models.IntegerField(null=True,blank=True)
    promo= models.BooleanField(default=False)
    pack= models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='photos')
    def __str__(self) : 
        return self.nom
    class Meta : 
        verbose_name = 'produit'

class demande (models.Model):
    nomprenom=models.CharField(max_length=500,blank=True,null=True)
    num=models.IntegerField(blank=True,null=True)
    adress=models.TextField(blank=True,null=True)
    pro=models.CharField(max_length=500,blank=True,null=True)
    class Meta : 
        verbose_name = 'demande'
