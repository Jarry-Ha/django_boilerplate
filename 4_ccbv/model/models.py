from django.contrib.auth import get_user_model
from django.db import models


class Verification(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    value = models.IntegerField('VAULE')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    def __str__(self):
        return self.title
