from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Entitat(models.Model):
    codi = models.IntegerField(null=False);
    nom = models.CharField(max_length=200, null=False);
    iban = models.CharField(max_length=24, null = False);
    email = models.CharField(max_length=200, null=True);
    telefon = models.DecimalField(max_digits=9, decimal_places=0,null=True);
    saldo_inicial = models.DecimalField(max_digits=9, decimal_places=2, null = True);
    saldo_ajuntament = models.DecimalField(max_digits=9, decimal_places=2, null = True);
    saldo_final = models.DecimalField(max_digits=9, decimal_places=2, null = True);
    def __str__(self):              # __unicode__ on Python 2
        return (self.nom);
        
    
class Moviments(models.Model):
    codiEnt = models.ForeignKey(Entitat, related_name='codiEnt' ,on_delete=models.CASCADE);
    data_mov = models.DateTimeField('Data del moviment');
    operacio = models.CharField(max_length = 500, null=False);
    ACCIO_CHOICES = (
        ('Entrada','Entrada'),
        ('Sortida','Sortida'),
        ('Traspas','Traspas'),
    )
    accio = models.CharField( max_length = 200, null=False, choices = ACCIO_CHOICES, default = 'Entrada' );
    _import = models.DecimalField(max_digits=9, decimal_places=2, null = True);
    conformitat = models.BooleanField(default=False);
    
    def save(self,val):
        if self.pk is not None:
            dat = Entitat.objects.get(entitat__id= self.codiEnt);
            dat.saldo_ajuntament += self._import;         
                
        super(Moviments, self).save(*args, **kwargs);

