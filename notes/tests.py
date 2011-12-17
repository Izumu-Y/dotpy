# -*- coding: utf8 *-*

from django.test import TestCase

from notes.models import Note

class NoteTest(TestCase):
    fixtures = ['notes_dev']

    def test_unicode(self):
        note = Note(content='Hello there!')
        self.assertEqual(note.__unicode__(), note.content)
        note.content = u'中文怎么样？' # TODO
        self.assertEqual(note.__unicode__(), note.content)
        note.content = ''
        self.assertEqual(note.__unicode__(), note.content)
        note.content = 'a' * 30
        self.assertEqual(note.__unicode__(), note.content)
        note.content = 'a' * 31
        self.assertEqual(note.__unicode__(), note.content[:27] + '...')
        note.content = 'a' * 100
        self.assertEqual(note.__unicode__(), note.content[:27] + '...')

    def test_notes(self):
        self.assertEqual(Note.all_objects.count(), 2)
