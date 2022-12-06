from django.db import models

"""
python manage.py inspectdb > models.py 명령어로\n
기존에 로컬 DB에 구축해둔 전체 뉴스와 댓글 데이터셋을 기반으로 만든 DB Table 명세입니다.
"""

class TbComment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    newsid = models.ForeignKey('TbNews', models.DO_NOTHING, db_column='NewsID')
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='UserID')
    writedat = models.DateTimeField(db_column='WritedAt', blank=True, null=True)
    content = models.TextField(db_column='Content', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_comment'


class TbDomain(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_domain'


class TbNews(models.Model):
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


class TbUser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    domainid = models.ForeignKey(TbDomain, models.DO_NOTHING, db_column='DomainID', blank=True, null=True)
    userid = models.CharField(db_column='UserID', max_length=16, blank=True, null=True)
    username = models.CharField(db_column='UserName', max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_user'