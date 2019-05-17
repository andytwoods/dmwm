from django.db import models


class Info(models.Model):

    Company_Name = models.TextField(blank=True, null=True)
    Employees = models.SmallIntegerField(blank=True, null=True)
    SIC_2007_Description = models.TextField(blank=True, null=True)
    Trading_Address = models.TextField(blank=True, null=True)
    Trading_Address_1 = models.TextField(blank=True, null=True)
    Trading_Address_2 = models.TextField(blank=True, null=True)
    Trading_Address_3 = models.TextField(blank=True, null=True)
    Trading_Address_4 = models.TextField(blank=True, null=True)
    Trading_Address_Postcode = models.TextField(blank=True, null=True)
    Trading_Post_Town = models.TextField(blank=True, null=True)
    Web_Address_1 = models.URLField(blank=True, null=True)

    Ready_To_Zoho = models.BooleanField(default=False)
    Uploaded_To_Zoho = models.BooleanField(default=True)
