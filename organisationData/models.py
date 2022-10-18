from django.db import models

# Create your models here.

class OrgType(models.Model):
    type = models.CharField('Organization Type', max_length=50)
    def __str__(self):
        return self.type

class OrgRegBy(models.Model):
    name        = models.CharField('Name', max_length=20)
    mailID      = models.EmailField('Email Address')
    def __str__(self):
        return self.name


class OrgData(models.Model):
    OrgID               = models.AutoField(primary_key=True)
    OrgName             = models.CharField('Organization Name', max_length=120)
    OrgAddress          = models.TextField(max_length=300)
    OrgEmail            = models.EmailField('E-mail Address')
    OrgContactNo        = models.CharField('Contact', max_length=11)
    OrgContactNoAlt     = models.CharField('Alternative Contact', max_length=11, blank=True, null=True)
    OrgType             = models.ForeignKey(OrgType, blank=True, null=True, on_delete=models.CASCADE)
    OrgRegBy            = models.ForeignKey(OrgRegBy, blank=False, null=False, on_delete=models.CASCADE)
    OrgCreated          = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)


    def __str__(self):
        return self.OrgName

class OrgAdmin(models.Model):
    OAID                = models.AutoField(primary_key=True, blank=False, null=False)
    OAname              = models.CharField("Name", max_length=120)
    OAUsername          = models.CharField("Username", max_length=120)
    OAEmail             = models.EmailField("Email Address")
    OAAddress           = models.TextField("Address", max_length=300)
    OAContactNo         = models.CharField("Contact", max_length=11)
    OAOrgName           = models.ForeignKey(OrgData, blank=False, null=False, on_delete=models.CASCADE)
    OAJoinedDate        = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    OAPassword          = models.CharField("Password", max_length=9)

    def __str__(self):
        return self.OAname
