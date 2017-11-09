from django.db import models

# Create your models here.
class Pc(models.Model):
	pc_num = models.IntegerField(db_column='PC_Num', primary_key=True)
	floor_num = models.IntegerField(db_column='Floor_Num',blank=True,null=True)
	
	class Meta:
		managed = False
		db_table = 'pc'