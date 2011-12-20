# -*- coding: utf8 *-*

from django.test import TestCase

from dotpy.notes.models import Note

class NoteTest(TestCase):
    fixtures = ['notes_dev']

    def test_unicode(self):
        note = Note(content='Hello there!')
        note.generate_html_content()
        self.assertEqual(note.__unicode__(), note.html_content)
        note.content = u'中文怎么样？' # TODO must use unicode string here?
        note.generate_html_content()
        self.assertEqual(note.__unicode__(), note.html_content)
        note.content = ''
        note.generate_html_content()
        self.assertEqual(note.__unicode__(), note.html_content)
        note.content = 'a' * 30
        note.generate_html_content()
        self.assertEqual(note.__unicode__(), note.html_content)
        note.content = 'a' * 31
        note.generate_html_content()
        self.assertEqual(note.__unicode__(), note.html_content[:27] + '...')
        note.content = 'a' * 100
        note.generate_html_content()
        self.assertEqual(note.__unicode__(), note.html_content[:27] + '...')

    def test_notes(self):
        self.assertEqual(Note.all_objects.count(), 2)

    def test_generate_html_content(self):
        note = Note()
        def _result(content, syntax):
            note.content = content
            note.syntax = syntax
            note.generate_html_content()
            return note.html_content
        # plain text
        self.assertEqual(_result("", 'plain'), "")
        self.assertEqual(_result(" ", 'plain'), "&nbsp;")
        self.assertEqual(_result("<script>", 'plain'), "&lt;script&gt;")
        self.assertEqual(_result("""{{{
print 'Hello'
}}}
<b>Hi</b>""", 'plain'), """<pre class="prettyprint">print &#39;Hello&#39;\n</pre>&lt;b&gt;Hi&lt;/b&gt;""")
        # reStructuredText
        self.assertEqual(_result("", 'rst'), "")
        self.assertEqual(_result("<script>", 'rst'), "<p>&lt;script&gt;</p>\n")
