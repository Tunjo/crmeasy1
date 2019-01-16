from django.db import models
from django.core.urlresolvers import reverse


class ItemStorage(models.Model):

    TYPE_LIST = (
        (1, 'Books'),
        (2, 'Beverage'),
        (3, 'Games')
    )

    name = models.CharField(max_length=30)
    disc = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    choice = models.PositiveSmallIntegerField(choices=TYPE_LIST)

    class Meta:
        verbose_name_plural = 'itemstorages'
        ordering = ('name', )
        unique_together = ('name', 'choice')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('item_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('item_edit', args=(self.id, ))

    def get_delete_url(self):
        return reverse('item_delete', args=(self.id,))

    def __str__(self):
        return "{} {}".format(self.name, self.created_on)


