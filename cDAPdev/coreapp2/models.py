from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

# Create your models here.

def upload_to_path(instance, filename):
    upload_to = r'script4apps/%s/%s' % (instance.author.username, filename)
    return upload_to


class Model_cdap(models.Model):
    author = models.ForeignKey(User, related_name='test_author')
    name = models.CharField(max_length=32,unique=True)
    title = models.CharField(max_length=255, null=True)

    type_class = (
        ('python', 'Python'),
        ('r', 'R'),
        ('knime', 'Knime'),
        ('spotfire', 'Spotfire'),
        ('excel','Excel'),
    )
    type = models.CharField(max_length=32, choices=type_class)

    modelpath = models.FileField(upload_to=upload_to_path, null=True)
    modelcmd = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    owner = models.CharField(max_length=32)
    #user = models.ForeignKey(User)
    description = models.TextField()
    pub_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        while Model_cdap.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num +=1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Model_cdap, self).save()


