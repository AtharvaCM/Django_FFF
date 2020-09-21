from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
# from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=100, default='')
#     city = models.CharField(max_length=100, default='')
#     website = models.URLField(default='')
#     phone = models.IntegerField(default=0)
#     image = models.ImageField(upload_to='profile_image', blank=True)

#     london = UserProfileManager()
#     objects = models.Manager()

#     def __str__(self):
#         return self.user.username


# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])


# post_save.connect(create_profile, sender=User)


class Profile(models.Model):
    # https://www.youtube.com/watch?v=FdVuKt_iuSI
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    # phone = models.IntegerField(default=0)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    image = models.ImageField(
        default='default_user.svg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        # https://www.youtube.com/watch?v=CQ90L5jfldw&t=105s
        super().save()

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
