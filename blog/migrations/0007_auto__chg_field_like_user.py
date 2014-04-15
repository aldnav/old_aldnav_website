# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Like.user'
        db.alter_column(u'blog_like', 'user', self.gf('django.db.models.fields.IPAddressField')(max_length=15))

    def backwards(self, orm):

        # Changing field 'Like.user'
        db.alter_column(u'blog_like', 'user', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True))

    models = {
        u'blog.like': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Like'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"}),
            'user': ('django.db.models.fields.IPAddressField', [], {'default': "'192.168.254.254'", 'max_length': '15', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'blog.tag': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Post']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['blog']