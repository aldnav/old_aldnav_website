import datetime
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length = 100, unique=True)
    slug = models.SlugField(editable=False, default='', unique=True)
    description = models.CharField(max_length = 100)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <  now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    def __unicode__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
    
        super(Post, self).save(*args, **kwargs)
    @models.permalink
    def get_absolute_url(self):
        return ('article', (), {
            'slug': self.slug,
            'id': self.id,
        })
    class Meta:
        ordering = ('pub_date',)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)
    
    def numInstances(self):
        return self.posts.all().count()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Like(models.Model):
    user = models.IPAddressField(default="192.168.254.254",blank=True)
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True)
 
    def __unicode__(self):
        return self.post.title
     
    class Meta:
        ordering = ('created',)