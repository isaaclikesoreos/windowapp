from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Customer(models.Model):
    AVATAR_CHOICES = [
        ('avatar1.png', 'Avatar 1'),
        ('avatar2.png', 'Avatar 2'),
        ('avatar3.png', 'Avatar 3'),
        ('avatar4.png', 'Avatar 4'),
        ('avatar5.png', 'Avatar 5'),
        ('avatar6.png', 'Avatar 6'),
        ('avatar7.png', 'Avatar 7'),
        ('avatar8.png', 'Avatar 8'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    selected_avatar = models.CharField(max_length=50, choices=AVATAR_CHOICES, null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    
    # Additional customer fields
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.displayname:
            return self.displayname
        return self.user.username

    @property
    def avatar(self):
        if self.selected_avatar:
            avatar_url = f'{settings.STATIC_URL}images/avatars/{self.selected_avatar}'
            return avatar_url
        elif self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg'
    


class Vehicle(models.Model):
    owner = models.ForeignKey(
        Customer,
        related_name='owned_vehicles',
        on_delete=models.CASCADE
    )
    vin = models.CharField(max_length=17, unique=True)  # Standard VIN length is 17 characters
    year = models.PositiveIntegerField()
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.vin}"
