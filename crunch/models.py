from enum import Enum

from django.db import models

Clusters_TTWA_Choice = (
    ('GA', "Guildford_and_Aldershot"),
    ('HW', "High_Wycombe_and_Aylesbury"),
    ('RE', "Reading"),
    ('SH', "Slough_and_Heathrow")
)
Clusters_TTWA_Choice_dict = {x: y for x, y in Clusters_TTWA_Choice}

Company_Focus_Area_Choice = (('AS', "Animation and SFX"),
                             ('AC', "AR/VR/MR Content"),
                             ('AH', "AR/VR/MR Hardware"),
                             ('AU', "Audio"),
                             ('CS', "Cultural Services"),
                             ('DA', "Digital Agency"),
                             ('FT', "Film / TV Production"),
                             ('GA', "Gaming"),
                             ('JO', "Journalism"),
                             ('MA', "Marketing Agency"),
                             ('NG', "Next Generation Technology"),
                             ('OT', "Other"),
                             ('TL', "Theatre/Life_Perf/Arts"),
                             )

Company_Focus_Area_Choice_dict = {x: y for x, y in Company_Focus_Area_Choice}

Within_Gateway_cluster_Choice = (('YE', "Yes"), ('NO', "No"), ('MA', "Marginal"))


Within_Gateway_cluster_Choice_dict = {x: y for x, y in Within_Gateway_cluster_Choice}


class ZohoInfo(models.Model):
    Company = models.CharField(blank=True, max_length=255, null=True)
    Trading_Address = models.CharField(blank=True, max_length=255, null=True)
    Trading_Town_City = models.CharField(blank=True, max_length=255, null=True)
    Trading_Post_Code = models.CharField(blank=True, max_length=255, null=True)
    Registered_Address = models.CharField(blank=True, max_length=255, null=True)
    Registered_Town_City = models.CharField(blank=True, max_length=255, null=True)
    Registered_Post_Code = models.CharField(blank=True, max_length=255, null=True)
    Email = models.EmailField(blank=True, null=True)
    Website = models.URLField(blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Twitter = models.CharField(blank=True, max_length=255, null=True)
    Company_Reg_Number_or_UTR = models.CharField(blank=True, max_length=255, null=True)
    Your_Company_SIC_Code = models.CharField(blank=True, max_length=255, null=True)

    Clusters_TTWA = models.CharField(max_length=5, choices=Clusters_TTWA_Choice, null=True, blank=True)
    Company_Focus_Area = models.CharField(max_length=5, choices=Company_Focus_Area_Choice, null=True, blank=True)
    Within_Gateway_cluster = models.CharField(max_length=5, choices=Within_Gateway_cluster_Choice, null=True, blank=True)

    Unqualified_Status = models.CharField(blank=True, max_length=255, null=True)
    Unqualified_Source = models.CharField(blank=True, max_length=255, null=True)
    Street = models.CharField(blank=True, max_length=255, null=True)
    City = models.CharField(blank=True, max_length=255, null=True)
    Province = models.CharField(blank=True, max_length=255, null=True)
    Postal_Code = models.CharField(blank=True, max_length=255, null=True)
    Country = models.CharField(blank=True, max_length=255, null=True, default='UK')
    Last_Name = models.CharField(blank=True, max_length=255, null=True, default='n/a')
    First_Name = models.CharField(blank=True, max_length=255, null=True, )
    Job_Title = models.CharField(blank=True, max_length=255, null=True, )

    No_of_Employees = models.SmallIntegerField(blank=True, null=True)
    Year_Company_Was_Founded = models.IntegerField(blank=True, null=True)

    Unqualified_Owner = models.CharField(blank=True, max_length=255, null=True, default='Marianna Rolbina')
    Unqualified_Owner_Id = models.IntegerField(blank=True, null=True, default='167499000000416001')
