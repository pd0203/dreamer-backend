from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        # Create a User with the given email & password
        if not email:
            raise ValueError(('Email address required'))
        user = self.model(
            email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password, **extra_fields):
        # Create a SuperUser with the given email & password
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

# Social Login User (NEW) User Model
class User(AbstractUser):
    name = models.CharField(max_length=30, unique=False)
    email = models.EmailField(max_length=50, unique=True)
    sns_type = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=10, null=True, blank=False)
    birthday = models.DateField(null=True, blank=False)
    is_male = models.BooleanField(null=True, default=True)
    mbti_id = models.ForeignKey('dreamer.MBTI', related_name='user', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    username = None
    first_name = None
    last_name = None
    date_joined = None

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'Users'
    def __str__(self):
        return self.email