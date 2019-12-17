from django.db import models

class Cliente(models.Model):

  nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  idade = models.IntegerField(
    default=0,
    null=False,
    blank=False
  )

  data_nascimento = models.DateField(
    blank=True,
    null=True
    )

  contado_responsavel = models.IntegerField(
    default=0,
    null=False,
    blank=False
  )

  endereco = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  telefone = models.IntegerField(
    default=0,
    null=False,
    blank=False
  )

  email = models.EmailField(
    max_length=254)

  escolaridade = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  profissao = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  religiao = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  orientacao_sexual = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

class Sessoes(models.Model):

    data_sessao = models.DateField(
        blank=True,
        null=True
        )

    objetivos = models.TextField()

    antecedente = models.CharField(
      max_length=255,
      null=False,
      blank=False
    )

    comportamento = models.CharField(
      max_length=255,
      null=False,
      blank=False
    )

    consequente = models.CharField(
      max_length=255,
      null=False,
      blank=False
    )

    intervencoes = models.TextField()

    recursos = models.TextField()
