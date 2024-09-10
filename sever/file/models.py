from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, userID, team,email, password=None, **extra):
        user = self.model(
            userID = userID,
            team  = team,
            email = self.normalize_email(email),
            **extra
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, userID, team,email ,password=None, **extra):
        extra.setdefault('is_admin', True)
        extra.setdefault('birth','2000-01-01')
        user = self.create_user(
            userID=userID,
            password = password,
            team = team,
            email= email,
            **extra
        )
        
        return user
    

class User(AbstractBaseUser):
    userID = models.CharField(verbose_name='ID', max_length=80, unique=True)
    team = models.CharField(verbose_name='TeamName', max_length=50)
    email = models.EmailField(verbose_name='email', max_length=80, blank=True)
    birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'userID'
    REQUIRED_FIELDS = ['team','email']

    def __str__(self):
        return self.userID
    
    def has_perm(self, perm ,obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
class Video(models.Model):
    video_file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_at
    