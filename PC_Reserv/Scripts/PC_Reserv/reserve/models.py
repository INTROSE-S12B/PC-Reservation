from django.db import models


# Create your models here.
class Floor(models.Model):
    floor_num = models.IntegerField(db_column='Floor_Num', primary_key=True)  # Field name made lowercase.
    floor_name = models.CharField(db_column='Floor_name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return 'Floor number:' + str(self.floor_num)

    class Meta:
        managed = False
        db_table = 'floor'


class Pc(models.Model):
    pc_id = models.AutoField(db_column='PC_ID', primary_key=True)  # Field name made lowercase.
    pc_num = models.IntegerField(db_column='PC_Num')  # Field name made lowercase.
    floor_num = models.ForeignKey(Floor, models.DO_NOTHING, db_column='Floor_Num')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pc'


class Reservation(models.Model):
    reservation_id = models.AutoField(db_column='Reservation_ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    id_year = models.CharField(db_column='ID_Year', max_length=3, blank=True, null=True)  # Field name made lowercase.
    college = models.CharField(db_column='College', max_length=3)  # Field name made lowercase.
    patron = models.CharField(db_column='Patron', max_length=45)  # Field name made lowercase.
    pc_num = models.ForeignKey(Pc, models.DO_NOTHING, db_column='PC_Num', related_name='PC')  # Field name made lowercase.
    floor_num = models.ForeignKey(Pc, models.DO_NOTHING, db_column='Floor_Num', related_name='Floor')  # Field name made lowercase.
    datetime_stamp = models.DateTimeField(db_column='DateTime Stamp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datetime_start = models.DateTimeField(db_column='DateTime Start', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservation'
