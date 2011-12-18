from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from dotpy.notes.models import Tag

class Project(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    votes = models.IntegerField(default=0)
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('project', [str(self.pk)])

    def get_description_str(self):
        """A readable description string."""
        if self.description is None or self.description == '':
            return _('No description set.')
        elif len(self.description) <= 30:
            return self.description
        else:
            return self.description[:27] + '...'
