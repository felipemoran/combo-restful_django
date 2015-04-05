from django.db import models
import os
import datetime
from django.utils import timezone
from django.contrib.auth.models import User, Group, Permission
from django.dispatch import receiver

# User._meta.get_field('username')._max_length = 75


tipos_de_compras = (
    ('normal', 'Normal'),
    ('cortesia', 'Cortesia'),
    ('reserva', 'Reserva'),
    ('----','----')
)

dia = (
    ('Segunda-Feira', "Segunda-Feira"),
    ('Terca-Feira', "Terca-Feira"),
    ('Quarta-Feira', "Quarta-Feira"),
    ('Quinta-Feira', "Quinta-Feira"),
    ('Sexta-Feira', "Sexta-Feira"),

)
class Faculdade(models.Model):
    nome = models.CharField("Faculdade", max_length=64)
    def __unicode__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField("Nome", max_length=64 )
    sobrenome = models.CharField("Sobrenome", max_length=256)
    faculdade = models.ForeignKey(Faculdade)
    ano_ingresso = models.IntegerField("Ano de ingresso")
    e_mail = models.CharField("E-mail", max_length=64)
    telefone = models.IntegerField("Telefone")
    curso = models.CharField("Curso", max_length=64)
    sacolinha = models.BooleanField(default=False)
    aceita_divulgacao = models.BooleanField(default=False)
    def __unicode__(self):
        return self.nome

class Atividade(models.Model):
    nome = models.CharField("Nome", max_length=64)
    dia = models.CharField("Dia", choices = dia, max_length = 64)
    horario = models.CharField("Horario", max_length=64)
    # descricao = models.CharField("Descricao",max_length=64)
    cap_participantes = models.IntegerField("Capacidade de Participantes")
    cap_atual = models.IntegerField("Capacidade Atual")
    pont_vendas = models.IntegerField("Pontuacao de Vendas", null=True, blank=True)
    preco = models.IntegerField("Preco")

    def __unicode__(self):
        return self.nome

    def cap_atual(self):
        compradas = Compra.objects.filter(atividade__nome=self.nome, comprado=True).count()
        reservadas = Compra.objects.filter(atividade__nome=self.nome, reservado=True).count()
        cortesias = Compra.objects.filter(atividade__nome=self.nome, cortesia=True).count()
        cap_inicial = self.cap_participantes
        cap_atual = cap_inicial - reservadas - cortesias - compradas

        return  cap_atual

    def reservas(self):
        reservas = Compra.objects.filter(atividade__nome=self.nome, reservado=True).count()

        return reservas

    def vendas(self):
        vendidos = Compra.objects.filter(atividade__nome=self.nome, comprado=True).count()
        cortesia = Compra.objects.filter(atividade__nome=self.nome, cortesia=True).count()
        vendas = vendidos + cortesia
        return vendas

class Email(models.Model):
    corpo = models.CharField("Corpo", max_length=512)
    assunto = models.CharField("Assunto", max_length=64)

    def __unicode__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField("Nome", max_length=64)
    def __unicode__(self):
        return self.nome


class PontodeVenda(models.Model):
    nome = models.CharField("Local de Venda", max_length=64)
    def __unicode__(self):
        return self.nome

class Compra(models.Model):
    participante = models.ForeignKey(Participante)
    atividade = models.ForeignKey(Atividade)
    tipo = models.CharField(choices = tipos_de_compras, max_length=64, default = "----", null = True, blank = True)
    local = models.ForeignKey(PontodeVenda, null = True, blank = True)
    vendedor = models.ForeignKey(Vendedor, null = True, blank = True)
    preco_pagar = models.IntegerField("Preco", null=True, blank=True)
    presente = models.BooleanField(default = False)
    comprado = models.BooleanField(default = False)
    reservado = models.BooleanField(default = False)
    cortesia = models.BooleanField(default = False)

    def __unicode__(self):
        return self.nome
