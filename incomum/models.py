# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faturamentosimplificado(models.Model):
    fim_codigo = models.IntegerField(primary_key=True)
    tur_codigo = models.IntegerField()
    loj_codigo = models.IntegerField()
    ven_codigo = models.IntegerField()
    age_codigo = models.IntegerField()
    fim_data = models.DateField()
    aco_codigo = models.IntegerField()
    fim_tipo = models.CharField(max_length=10)
    tur_numerovenda = models.CharField(max_length=20)
    fim_valorliquido = models.FloatField()
    fim_markup = models.FloatField()
    fim_valorinc = models.FloatField()
    fim_valorincajustado = models.FloatField()
    loj_descricao = models.CharField(max_length=10)
    aco_descricao = models.CharField(max_length=20)
    ven_descricao = models.CharField(max_length=40)
    age_descricao = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'faturamentosimplificado'


class IncomumAgencia(models.Model):
    age_codigo = models.AutoField(primary_key=True)
    age_viagem = models.CharField(max_length=70)
    age_site = models.CharField(max_length=180, blank=True, null=True)
    age_datacadastro = models.CharField(max_length=255, blank=True, null=True)
    age_cnpj = models.CharField(max_length=20)
    age_situacao = models.CharField(max_length=20)
    age_inscricaomunicipal = models.CharField(max_length=20, blank=True, null=True)
    age_cep = models.IntegerField(blank=True, null=True)
    age_rua = models.CharField(max_length=70, blank=True, null=True)
    age_numero = models.IntegerField(blank=True, null=True)
    age_bairro = models.CharField(max_length=70, blank=True, null=True)
    age_cidade = models.CharField(max_length=50, blank=True, null=True)
    age_fone = models.IntegerField(blank=True, null=True)
    age_celular = models.IntegerField(blank=True, null=True)
    age_comissao = models.FloatField()
    age_over = models.FloatField(blank=True, null=True)
    age_markup = models.FloatField(blank=True, null=True)
    age_banco = models.CharField(max_length=20)
    age_agencia = models.IntegerField(blank=True, null=True)
    age_conta = models.IntegerField(blank=True, null=True)
    def save(self, *args, **kwargs):
        # Verifica se o valor do campo é uma string vazia e, se sim, substitui por 0
        if self.age_cep == '':
            self.age_cep = 0
        if self.age_numero == '':
            self.age_numero = 0
        if self.age_fone == '':
            self.age_fone = 0
        if self.age_celular == '':
            self.age_celular = 0
        if self.age_agencia == '':
            self.age_agencia = 0
        if self.age_conta == '':
            self.age_conta = 0
        if self.age_over == '':
            self.age_over = 0
        if self.age_markup == '':
            self.age_markup = 0
        super().save(*args, **kwargs)
    

    class Meta:
        managed = True
        db_table = 'incomum_agencia'


class IncomumAgente(models.Model):
    agt_codigo = models.AutoField(primary_key=True)
    age_codigo = models.CharField(max_length=255)
    agt_descricao = models.CharField(max_length=255)
    agt_cpf = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'incomum_agente'


class IncomumUsuario(models.Model):
    nome = models.TextField()
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'incomum_usuario'


class Turisticosituacao(models.Model):
    tur_codigo = models.IntegerField(primary_key=True)  # The composite primary key (tur_codigo, tsi_codigo) found, that is not supported. The first column is selected.
    tsi_codigo = models.IntegerField()
    tsi_datacadastro = models.DateField()
    usr_codigo = models.IntegerField()
    stu_codigo = models.IntegerField()
    tsi_observacao = models.CharField(max_length=90, blank=True, null=True)
    tsi_markup = models.FloatField(blank=True, null=True)
    tsi_valorcambio = models.FloatField(blank=True, null=True)
    tsi_comissao = models.FloatField(blank=True, null=True)
    tsi_valortaxa = models.FloatField(blank=True, null=True)
    tsi_taxaemissao = models.FloatField(blank=True, null=True)
    tsi_incentivo = models.FloatField(blank=True, null=True)
    tsi_valortarifa = models.FloatField(blank=True, null=True)
    tsi_valorliquido = models.FloatField(blank=True, null=True)
    tsi_valorinc = models.FloatField()
    tsi_valorbase = models.FloatField(blank=True, null=True)
    tsi_valorprejuizo = models.FloatField(blank=True, null=True)
    tsi_markupajustado = models.FloatField(blank=True, null=True)
    tsi_vendareal = models.FloatField(blank=True, null=True)
    tsi_comissaoreal = models.FloatField(blank=True, null=True)
    tsi_incentivoreal = models.FloatField(blank=True, null=True)
    tsi_arredondamentoreal = models.FloatField(blank=True, null=True)
    tsi_diferencacambioreal = models.FloatField(blank=True, null=True)
    tsi_diferencaavista = models.FloatField(blank=True, null=True)
    tsi_incajustado = models.FloatField(blank=True, null=True)
    tsi_diferencataxareal = models.FloatField(blank=True, null=True)
    tsi_percentualcomissao = models.FloatField(blank=True, null=True)
    tsi_percentualincentivo = models.FloatField(blank=True, null=True)
    tsi_cambiotaxareal = models.FloatField(blank=True, null=True)
    tsi_multaincomum = models.FloatField(blank=True, null=True)
    tsi_netoreembolso = models.FloatField(blank=True, null=True)
    tsi_taxareembolso = models.FloatField(blank=True, null=True)
    tsi_vendareembolso = models.FloatField(blank=True, null=True)
    tsi_comissaoreembolso = models.FloatField(blank=True, null=True)
    tsi_incentivoreembolso = models.FloatField(blank=True, null=True)
    tsi_custoajustado = models.FloatField(blank=True, null=True)
    tsi_valoroperacional = models.FloatField(blank=True, null=True)
    tsi_valornota = models.FloatField(blank=True, null=True)
    tsi_valornotaajustado = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'turisticosituacao'
        unique_together = (('tur_codigo', 'tsi_codigo'),)
