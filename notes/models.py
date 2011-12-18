from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

class PublicNoteManager(models.Manager):
    def get_query_set(self):
        return super(PublicNoteManager, self).get_query_set().filter(is_private=False)

class Note(models.Model):
    content = models.TextField()
    is_private = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    all_objects = models.Manager()
    public_objects = PublicNoteManager()

    def __unicode__(self):
        if len(self.content) <= 30:
            return self.content
        else:
            return self.content[:27] + '...'

    @models.permalink
    def get_absolute_url(self):
        return ('note', [str(self.id)])
