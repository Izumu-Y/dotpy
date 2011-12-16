from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return u'{}'.format(self.name)

class Note(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        if len(self.content) <= 30:
            return u'{}'.format(self.content)
        else:
            return u'{}...'.format(self.content[:27])
