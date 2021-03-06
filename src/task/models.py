from django.db import models
from .managers import TaskManager
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    STATE_PENDING = 'Pendiente'
    STATE_RUNNING = 'Ejecutándose'
    STATE_INCOMPLETE = 'Incompleta'
    STATE_FINISHED = 'Terminada'
    STATE_FINISHED_WITH_ERROR = 'Terminada debido a un error'
    STATE_CHOICES = (
        (STATE_PENDING, STATE_PENDING),
        (STATE_INCOMPLETE, STATE_INCOMPLETE),
        (STATE_RUNNING, STATE_RUNNING),
        (STATE_FINISHED, STATE_FINISHED),
        (STATE_FINISHED_WITH_ERROR, STATE_FINISHED_WITH_ERROR),
    )

    TYPE_CRAWLER = 'Crawler'
    TYPE_CHOICES = (
        (TYPE_CRAWLER, 'Crawler'),
    )

    pid = models.PositiveIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete="cascade")
    username = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, default='', blank=True)
    description = models.CharField(max_length=200, null=True, default='', blank=True)
    result = models.IntegerField(null=True, default=0, blank=True)
    error = models.CharField(max_length=200)
    state = models.CharField(
        max_length=30,
        choices=STATE_CHOICES,
        default=STATE_PENDING,
        null=True,
        blank=True,
    )

    type = models.CharField(
        max_length=23,
        choices=TYPE_CHOICES,
        default='',
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True)  # models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True, default=None)  # models.DateTimeField(auto_now=True)

    objects = TaskManager()
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_at', 'state']  # El - delante del nombre del atributo indica que se o
        # unique_together = (('id'),)



    def __str__(self):
        return f'{self.pid} - {self.type} - {self.state} - {self.created_at}'

    @property
    def is_running(self):
        return self.state == Task.STATE_RUNNING

    @property
    def is_completed(self):
        return self.state == Task.STATE_FINISHED

