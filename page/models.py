from django.db import models
from django.utils import timezone
from . import utils
from acesso.models import Usuario

class Categoria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    categoria = models.CharField(max_length=50, verbose_name="Categoria")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Categoria: {}".format(self.categoria)

class Saidas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    valor = models.DecimalField(verbose_name="Valor Saída", max_digits=11, decimal_places=2)
    data = models.DateField(verbose_name="Data", default=timezone.now().date())
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descricao = models.CharField(verbose_name="Descrição", max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['usuario','-data', 'categoria', 'valor']

    def __str__(self):
        return "Usuário: {} | Saída: {} ({})".format(self.usuario, self.valor, self.categoria.categoria)

class Entradas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    valor = models.DecimalField(verbose_name="Valor Entrada", max_digits=11, decimal_places=2)
    data = models.DateField(verbose_name="Data", default=timezone.now().date())
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descricao = models.CharField(verbose_name="Descrição", max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['usuario','-data', 'categoria', 'valor']
        
    def __str__(self):
        return "Usuário: {} | Entrada: {} ({})".format(self.usuario, self.valor, self.categoria.categoria)