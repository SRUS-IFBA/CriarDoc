from django.db import models

class Base(models.Model):
    id= models.AutoField(primary_key=True)
    introducao = models.TextField (blank = False)
    desc_qualidade = models.TextField (blank = False)

    def __unicode__(self):

    class Meta:

class Tecnologias(models.Model):
    id = models.AutoField(primary_key=True)
	tecnologia = models.CharField(max_length=200)
	justificativa = models.TextField(blank=False)
	base = models.ForeignKey(Base)

	def __unicode__(self):
		return '%s' % self.tecnologia

	class Meta:
	db_table = 'tecnologia'
	verbose_name = 'Tecnologias'
	verbose_name_plural = 'Tecnologias'
	ordering = ['tecnologia']
