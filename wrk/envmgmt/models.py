from django.db import models


class Project(models.Model):
    prg_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.project_name


class EnvHdr(models.Model):

    TIER = (
        ('DEV', 'Development'),
        ('TEST', 'Testing'),
        ('QA', 'QA'),
        ('TRAIN', 'Training'),
        ('PROD', 'Proudction'),
    )
    OWNER = (
        ('INTERNAL', 'Internal'),
        ('CUSTOMER', 'Customer'),
    )

    project_name = models.ForeignKey('Project', on_delete=models.CASCADE)
    env_owner = models.CharField(max_length=40, choices=OWNER)
    env_tier = models.CharField(max_length=100, choices=TIER)
    env_location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s %s - %s" % (self.project_name, self.env_owner, self.env_tier, self.env_location)


class EnvDtl(models.Model):

    PRODUCT = (
        ('WM', 'Warehouse Management'),
        ('WFM', 'Workforce Management'),
        ('EMS', 'Event Management'),
        ('HUB', 'HUB'),
        ('RPT', 'Report'),
        ('REFS', 'REFS'),
    )

    OS = (
        ('WINDOWS 2008', 'Windows Server 2008'),
        ('WINDOWS 2012', 'Windows Server 2012'),
        ('WINDOWS 2016', 'Windows Server 2016'),
        ('RHEL 7', 'Red Hat Linux 7'),
        ('RHEL 6', 'Red Hat Linux 6'),
        ('AIX 6', 'AIX 6'),
        ('AIX 7', 'AIX 7'),
    )

    env_tier = models.ForeignKey('EnvHdr', on_delete=models.CASCADE)
    app_product = models.CharField(max_length=100, choices=PRODUCT)
    app_server1 = models.CharField(max_length=100, blank=False)
    app_server2 = models.CharField(max_length=100, blank=True)
    app_os = models.CharField(max_length=100, choices=OS)
    app_cluster = models.IntegerField(default=0)
    app_port = models.CharField(max_length=100)
    refs_url = models.CharField(max_length=100)
    db_name = models.CharField(max_length=100, blank=False)
    db_server1 = models.CharField(max_length=100, blank=False)
    db_server2 = models.CharField(max_length=100, blank=True)
    db_type = models.CharField(max_length=100, blank=False)
    db_os = models.CharField(max_length=100, choices=OS)

    def __str__(self):
        return "%s %s %s" % (self.env_tier, self.app_product, self.app_server1)


class Patch(models.Model):
    patch_release = models.CharField(max_length=100)
    patch_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.env_tier, self.patch_release)


class EnvPatch(models.Model):
    env_tier = models.ForeignKey('EnvDtl', on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    errors = models.IntegerField(blank=True)