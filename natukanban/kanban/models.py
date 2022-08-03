from django.db import models
from django.utils import timezone


# função para definir a data de vencimento da Task por padrão
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class Board(models.Model):
    name = models.CharField(max_length=50)

class Column(models.Model):
    title = models.CharField(max_length=255)
    board = models.ForeignKey("Board", related_name="columns", on_delete=models.CASCADE)

class Task(models.Model):
    
    # (armazenado no banco de dados, visualização do usuário)
    category_options = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    category = models.CharField(max_length=25, choices=category_options, default='importante')
    status = models.ForeignKey(Column, related_name="tasks", on_delete=models.CASCADE)

