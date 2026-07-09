from django.db import models


class CustomerInquiry(models.Model):

    SERVICE_CHOICES = [
        ('Window', 'Window'),
        ('Door', 'Door'),
        ('Ceiling', 'Ceiling'),
        ('Glass', 'Glass'),
        ('Other', 'Other'),
    ]


    name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    location = models.CharField(max_length=200)

    service = models.TextField()

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
