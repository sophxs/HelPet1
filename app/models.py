from django.db import models
from django.utils.timezone import now

class User(models.Model):
    code = models.AutoField(db_column='cd_user', primary_key=True)
    email = models.CharField(max_length=100, db_column='email_user')
    name = models.CharField(max_length=100, db_column='nm_user')
    password = models.CharField(max_length=60, db_column='ps_user')
    date_ins = models.DateField(db_column='dt_insert', default=now())

    class Meta:
        db_table = 'tb_USER'