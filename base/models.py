from django.db import models

class Base(models.Model):
    id= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150,blank = False)
    introducao = models.TextField (blank = False)
    desc_qualidade = models.TextField (blank = False)
    desc_ponto_sensibilidade = models.TextField (blank = False)
    desc_nao_riscos = models.TextField (blank = False)
    desc_riscos = models.TextField (blank = False)
    desc_arquitetura_texto = models.TextField(blank = False)
    desc_arquitetura = models.ImageField(upload_to="destino")
    desc_pricipais_abordagens_arquitetura = models.TextField (blank = False)
    desc_pontos_trade_off = models.TextField (blank = False)

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
