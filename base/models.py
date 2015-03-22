from django.db import models

class Base(models.Model):
    id= models.AutoField(primary_key=True)
    introducao = models.TextField (blank = false)
    desc_qualidade = models.TextField (blank = false)
    desc_ponto_sensibilidade = models.TextField (blank = false)

    def __unicode__(self):

	class Meta:

#teste de abnerrr
