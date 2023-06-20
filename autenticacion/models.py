from django.db import models

class IPAddress(models.Model):
    ip_address = models.CharField(max_length=200)

    class Meta:
        db_table = "ipaddress"
