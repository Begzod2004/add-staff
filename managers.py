from django.db.models import Value, Case, When,F,Manager
from django.contrib.auth.models import BaseUserManager
from django.db.models.functions import Concat,Substr
from django.db.models.query import QuerySet


class CustomUserManager(BaseUserManager):
    
    def get_fullname(self):
        return self.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))

    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError("Phone fields is required")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone, password, **extra_fields)

class UserQueryset(QuerySet):
    def get_info(self):
        return self.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name'),
            phone_number=Concat(
                Value('+998'),
                Value(' ('),
                Substr(F('phone'),1,2),
                Value(') '),
                Substr(F('phone'),3,3),
                Value(' '),
                Substr(F('phone'),6,2),
                Value(' '),
                Substr(F('phone'),8,2)
                )
        )
    def users(self,id):
        return self.get_info().exclude(id=id) 

    def user(self,id):
        return self.get_info().filter(id=id).first()

class UserManager(Manager):
    def get_query_set(self):
        return UserQueryset(self.model)
    
    def users(self,id):
        return self.get_query_set().users(id)

    def user(self,id):
        return self.get_query_set().user(id)    