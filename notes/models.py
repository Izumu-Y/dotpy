from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape, strip_tags
from django.utils.translation import ugettext as _

from docutils.core import publish_parts
import re

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
        result = strip_tags(self.html_content)
        if len(result) <= 30:
            return result
        else:
            return result[:27] + '...'

    @models.permalink
    def get_absolute_url(self):
        return ('note', [str(self.id)])

    def save(self, *args, **kwargs):
        self.generate_html_content()
        super(Note, self).save(*args, **kwargs)

    @staticmethod
    def _parse_plain(raw_content):
        if not raw_content:
            return ""
        lines = []
        in_code = False
        for line in raw_content.split("\n"):
            if in_code:
                m = re.match(r'\}\}\}$', line)
                if m:
                    lines.append('</pre>')
                    in_code = False
                else:
                    lines.append(escape(line))
                    lines.append("\n")
            else:
                m = re.match(r'\{\{\{$', line)
                if m:
                    in_code = True
                    lines.append('<pre class="prettyprint">')
                else:
                    lines.append(escape(line).replace("\n", "<br/>").replace(" ", "&nbsp;").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;"))
        return "".join(lines)

    def generate_html_content(self):
        if self.syntax == 'rst':
            # TODO process code syntax highlighting
            self.html_content = publish_parts(self.content, writer_name='html')['body']
        else:
            # plain text (or other unexpected syntax)
            self.html_content = Note._parse_plain(self.content)
