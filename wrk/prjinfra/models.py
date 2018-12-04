from django.db import models

TIER = (
    ('DEV', 'Development'),
    ('TEST', 'Testing'),
    ('QA', 'Quality Assurance'),
    ('PROD', 'Production'),
)


class Project(models.Model):
    prj_name = models.CharField(max_length=50)

    def __str__(self):
        return self.prj_name


class Server(models.Model):

    SRV_FUNCTION = (
        ('APP', 'Application'),
        ('DB', 'Database'),
    )

    SRV_OS = (
        ('WINDOWS 2008', 'Windows Server 2008'),
        ('WINDOWS 2012', 'Windows Server 2012'),
        ('WINDOWS 2016', 'Windows Server 2016'),
        ('RHEL 7', 'Red Hat Linux 7'),
        ('RHEL 6', 'Red Hat Linux 6'),
    )

    SRV_OWNER = (
        ('INTERNAL', 'Internal'),
        ('EXTERNAL', 'External'),
    )

    prj = models.ForeignKey('Project', on_delete=models.CASCADE)
    srv_name = models.CharField(max_length=30)
    srv_owner = models.CharField(max_length=30, choices=SRV_OWNER)
    srv_function = models.CharField(max_length=25, choices=SRV_FUNCTION)
    srv_os = models.CharField(max_length=30, choices=SRV_OS)

    def __str__(self):
        return "%s - %s" % (self.srv_name, self.srv_function)


class Application(models.Model):

    APP = (
        ('WM', 'Warehouse Management'),
        ('WFM', 'Workforce Management'),
        ('EMS', 'Event Management'),
        ('REFS', 'Refs Web')
    )

    prj = models.ForeignKey('Project', on_delete=models.CASCADE)
    srv = models.ForeignKey('Server', on_delete=models.CASCADE)
    sys_account = models.CharField(max_length=25)
    tier = models.CharField(max_length=25, choices=TIER)
    app = models.CharField(max_length=25, choices=APP)
    app_version = models.CharField(max_length=100)
    app_path = models.CharField(max_length=100)
    app_port = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (self.srv, self.tier)


class Database(models.Model):

    DBTYPE = (
        ('SQL SERVER', 'Microsoft SQL Server'),
        ('ORACLE', 'Oracle'),
    )

    prj = models.ForeignKey('Project', on_delete=models.CASCADE)
    srv = models.ForeignKey('Server', on_delete=models.CASCADE)
    sys_account = models.CharField(max_length=25)
    tier = models.CharField(max_length=25, choices=TIER)
    dbms = models.CharField(max_length=25, choices=DBTYPE)
    dbms_version = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s - %s" % (self.prj, self.srv, self.dbms)


class Rollout(models.Model):

    rollout_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rollout_name


class RolloutDtls(models.Model):

    rollout_name = models.ForeignKey('Rollout', on_delete=models.CASCADE)
    jira_num = models.CharField(max_length=100)
    jira_url = models.URLField()

    def __str__(self):
        return "%s - %s" % (self.rollout_name, self.jira_num)


class RolloutTrans(models.Model):
    srv_name = models.ForeignKey('Server', on_delete=models.CASCADE)
    rollout_name = models.ForeignKey('Rollout', on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s" % (self.srv_name, self.rollout_name, self.applied_date)