from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Face(models.Model):
    chin_angle = models.FloatField()
    mofa_ratio = models.FloatField()
    hlmo_angle = models.FloatField()
    shape = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name = "faces", on_delete='CASCADE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Face object: {} {} {} {} {} {}>".format(self.chin_angle, self.mofa_ratio, self.hlmo_angle, self.shape, self.image, self.user)