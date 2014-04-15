# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Post', fields ['slug']
        db.delete_unique(u'blog_post', ['slug'])

        # Adding model 'Tag'
        db.create_table(u'blog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Tag'])

        # Adding M2M table for field posts on 'Tag'
        m2m_table_name = db.shorten_name(u'blog_tag_posts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'post_id'])


        # Changing field 'Post.slug'
        db.alter_column(u'blog_post', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'blog_tag')

        # Removing M2M table for field posts on 'Tag'
        db.delete_table(db.shorten_name(u'blog_tag_posts'))


        # Changing field 'Post.slug'
        db.alter_column(u'blog_post', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, null=True))
        # Adding unique constraint on 'Post', fields ['slug']
        db.create_unique(u'blog_post', ['slug'])


    models = {
        u'blog.post': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'}),
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