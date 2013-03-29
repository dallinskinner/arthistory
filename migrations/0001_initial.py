# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artwork'
        db.create_table(u'study_helper_artwork', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study_helper.Artist'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['study_helper.Category'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'study_helper', ['Artwork'])

        # Adding model 'Artist'
        db.create_table(u'study_helper_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'study_helper', ['Artist'])

        # Adding model 'Category'
        db.create_table(u'study_helper_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'study_helper', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Artwork'
        db.delete_table(u'study_helper_artwork')

        # Deleting model 'Artist'
        db.delete_table(u'study_helper_artist')

        # Deleting model 'Category'
        db.delete_table(u'study_helper_category')


    models = {
        u'study_helper.artist': {
            'Meta': {'object_name': 'Artist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'study_helper.artwork': {
            'Meta': {'object_name': 'Artwork'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['study_helper.Artist']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['study_helper.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'study_helper.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['study_helper']