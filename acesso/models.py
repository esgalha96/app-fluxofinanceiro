from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email,password=None, cpf=None, phone=None, cep=None):
        if not email:
            raise ValueError('O usuário deve ter um endereço de email válido.')

        user = self.model(
            username = username,
            email = email,
            cpf=cpf,
            phone=phone,
            cep=cep
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, cpf=None, phone=None, cep=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            cpf=cpf,
            phone=phone,
            cep=cep,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, verbose_name="Usuário")
    email = models.EmailField(max_length=255, unique=True, verbose_name="E-mail")
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nome")
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Sobrenome")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="Telefone")
    cep = models.CharField(max_length=15, blank=False, null=False, verbose_name="CEP")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    is_admin = models.BooleanField(default=False, verbose_name="Admin")

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','cpf', 'phone','cep']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    def is_superuser(self):
        return self.is_admin