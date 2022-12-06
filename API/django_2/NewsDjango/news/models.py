from django.db import models

class News(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    domainid = models.ForeignKey(TbDomain, models.DO_NOTHING, db_column='DomainID')
    maincategory = models.CharField(db_column='MainCategory', max_length=16, blank=True, null=True)
    subcategory = models.CharField(db_column='SubCategory', max_length=16, blank=True, null=True)
    writedat = models.DateTimeField(db_column='WritedAt', blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=128, blank=True, null=True)
    content = models.TextField(db_column='Content')
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)
    photourl = models.TextField(db_column='PhotoURL', blank=True, null=True)
    writer = models.CharField(db_column='Writer', max_length=16, blank=True, null=True)
    stickers = models.TextField(db_column='Stickers', blank=True, null=True)
    press = models.CharField(db_column='Press', max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_news'
