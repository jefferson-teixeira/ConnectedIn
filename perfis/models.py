from django.db import models

# Create your models here.
class Perfil(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    empresa = models.CharField(max_length=100)
    contatos = models.ManyToManyField('self')

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()
