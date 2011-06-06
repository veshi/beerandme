from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=200)
    competition_date = models.DateField()
    total_entries = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'%s -- %s' % (self.name, self.competition_date)

    class Meta:
        unique_together = (('name', 'competition_date'),)

class Judge(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.name


class Brewer(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

class Beer(models.Model):
    name = models.CharField(max_length=200)
    bjcp = models.CharField(max_length=4, verbose_name='BJCP')
    brewers = models.ManyToManyField(Brewer)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.bjcp)

class Attribute(models.Model):
    name = models.CharField(max_length=200)
    max_rating = models.IntegerField(default=10)

    def __unicode__(self):
        return u'%s' % self.name

class Rating(models.Model):
    rating = models.IntegerField()
    comments = models.TextField(blank=True)
    attribute = models.ForeignKey(Attribute)
    beer = models.ForeignKey(Beer)
    competition = models.ForeignKey(Competition)
    judge = models.ForeignKey(Judge)

    def __unicode__(self):
        return u'%s -- %s: %d/%d' % (self.beer, self.attribute.name, 
                self.rating, self.attribute.max_rating)

