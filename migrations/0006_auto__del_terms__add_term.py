# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Terms'
        db.delete_table(u'study_helper_terms')

        # Adding model 'Term'
        db.create_table(u'study_helper_term', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'study_helper', ['Term'])


    def backwards(self, orm):
        # Adding model 'Terms'
        db.create_table(u'study_helper_terms', (
            ('term', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'study_helper', ['Terms'])

        # Deleting model 'Term'
        db.delete_table(u'study_helper_term')


    models = {
        u'study_helper.artist': {
            'Meta': {'object_name': 'Artist'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'study_helper.artwork': {
            'Meta': {'object_name': 'Artwork'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['study_helper.Artist']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['study_helper.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'unit': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'study_helper.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'study_helper.term': {
            'Meta': {'object_name': 'Term'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['study_helper']