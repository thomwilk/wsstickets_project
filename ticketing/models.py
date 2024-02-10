from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    unit = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    tenant_name = models.CharField(max_length=100, blank=True, null=True)
    entry_permission = models.BooleanField(default=True,)

    def __str__(self):
        return f"{self.building.name} Unit {self.unit} - {self.status}"

class Reply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.ticket.building.name} Unit {self.ticket.unit} - {self.author} - {self.created_at}"