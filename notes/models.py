from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.translation import ugettext as _

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

class PublicNoteManager(models.Manager):
    def get_query_set(self):
        return super(PublicNoteManager, self).get_query_set().filter(is_private=False)

class Note(models.Model):
    content = models.TextField()
    html_content = models.TextField()
    is_private = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    SYNTAX_CHOICES = (
        ('plain', _('plain text')),
        ('rst', _('reStructuredText')),
    )
    syntax = models.CharField(max_length=10, choices=SYNTAX_CHOICES, default='plain')
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

    def save(self, *args, **kwargs):
        self.html_content = Note.generate_html_content(self.content, self.syntax)
        super(Note, self).save(*args, **kwargs)

    @staticmethod
    def generate_html_content(raw_content, syntax):
        # TODO process code syntax highlighting
        if syntax == 'rst':
            # TODO process rst
            return escape(raw_content)
        else:
            # plain text (or other unexpected syntax)
            return escape(raw_content).replace("\n", "<br/>").replace(" ", "&nbsp;").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
