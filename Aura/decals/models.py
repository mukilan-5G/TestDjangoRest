from __future__ import unicode_literals
import os

from django.db import models


def update_filename_side(instance, filename):
    path = 'images/parts/'
    format = str(instance.part.name) +\
        str(instance.side)\
        + '.xlsx'
    return os.path.join(path, format)


def update_filename_decal(instance, filename):
    path = 'images/decals/'
    format = str(instance.name) + '.xlsx'
    return os.path.join(path, format)


class Part(models.Model):
    name = models.CharField(max_length=60)
    number = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_updated = models.BooleanField(default=False)

    class Meta:
        db_table = 'Part'

    def __unicode__(self):
        return u'%s-%s' % (self.number, self.name)


SIDE_CHOICES = (
    ('top', 'Top'),
    ('bottom', 'Bottom'),
    ('left', 'Left'),
    ('right', 'Right')
)


class PartSide(models.Model):
    part = models.ForeignKey(
        Part, on_delete=models.CASCADE)
    side = models.CharField(max_length=6, choices=SIDE_CHOICES)
    no_of_decals = models.IntegerField()
    template_number = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True, editable=True)
    Revised_on = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)
    is_updated = models.BooleanField(default=False)
    image = models.FileField(
        upload_to=update_filename_side,
    )

    class Meta:
        db_table = 'PartSide'
        unique_together = ('part', 'side')

    def admin_image(self):
        return '<img src="%s"/>' % self.image.path
    admin_image.allow_tags = True

    def __unicode__(self):
        return u'%s-%s' % (self.part.name, self.side)


class DecalCategory(models.Model):
    name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_updated = models.BooleanField(default=False)

    class Meta:
        db_table = 'DecalCategory'

    def __unicode__(self):
        return u'%s-%s' % (self.name)


class Decal(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(
        DecalCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_updated = models.BooleanField(default=False)
    image = models.FileField(
        upload_to=update_filename_decal,
    )

    class Meta:
        db_table = 'Decal'

    def __unicode__(self):
        return u'%s-%s' % (self.category, self.name)


class PartSideDecal(models.Model):
    part_side = models.ForeignKey(
        PartSide, on_delete=models.CASCADE)
    decal = models.ForeignKey(
        Decal, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_updated = models.BooleanField(default=False)

    class Meta:
        db_table = 'PartSideDecal'

    def __unicode__(self):
        return u'%s-%s' % (self.part_side.side, self.decal.name)
