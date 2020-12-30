from django.db import models

# Create your models here.
class donor(models.Model):
    d_name=models.CharField(max_length=25)
    d_age=models.IntegerField()
    sex=models.CharField(max_length=10)
    weight = models.IntegerField()
    d_address = models.CharField(max_length=40,null=True)
    d_dob = models.DateField()
    d_phone_no = models.CharField(max_length=15)
    med_hist=models.CharField(max_length=40)


    def __str__(self):
        return self.d_name

class bloodbank(models.Model):
    bb_name = models.CharField(max_length=30)
    bb_phone_no=models.CharField(max_length=15)
    bb_address=models.CharField(max_length=40)
    bb_Email=models.CharField(max_length=15)


    def __str__(self):
        return self.bb_name

class blood(models.Model):
    bb_id = models.ForeignKey(bloodbank, on_delete=models.CASCADE)
    donor_id=models.ForeignKey(donor, on_delete=models.CASCADE)
    bld_type=models.CharField(max_length=3)
    date=models.DateField()
    time=models.TimeField()
    bld_qty = models.IntegerField()



    def __str__(self):
        return self.bld_type

#
class hospital(models.Model):
    h_name = models.CharField(max_length=30, unique=True)
    h_phone_no=models.CharField(max_length=15)
    h_address=models.CharField(max_length=40)


    def __str__(self):
        return self.h_name

class employee(models.Model):
    bb_id=models.ForeignKey(bloodbank, on_delete=models.CASCADE)
    e_name = models.CharField(max_length=30)
    e_phone_no=models.CharField(max_length=15)
    e_Address=models.CharField(max_length=40)
    e_email=models.CharField(max_length=40)
    position=models.CharField(max_length=20)



    def __str__(self):
        return self.e_name


class order(models.Model):
    hospital_id = models.ForeignKey(hospital, on_delete=models.CASCADE)
    date = models.DateField()
    quantity=models.IntegerField()
    bld_typ_req=models.CharField(max_length=3)
    recipient_name=models.CharField(max_length=20)

    def __str__(self):
        return self.recipient_name

