from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=200)
    competition_date = models.DateField()
    total_entries = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'%s -- %s' % (self.name, self.competition_date)

    class Meta:
        unique_together = (('name', 'competition_date'),)

class JudgeRank(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

class Descriptor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name

class Judge(models.Model):
    name = models.CharField(max_length=200)
    bjcp_id = models.CharField(max_length=200, verbose_name='BJCP ID', blank=True)
    rank = models.ForeignKey(JudgeRank)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name

class Brewer(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

class Beer(models.Model):
    name = models.CharField(max_length=200)
    brewers = models.ManyToManyField(Brewer)
    url = models.URLField(verbose_name='URL', blank=True)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name

class Attribute(models.Model):
    name = models.CharField(max_length=200)
    max_rating = models.IntegerField(default=10)

    def __unicode__(self):
        return u'%s' % self.name

class Entry(models.Model):
    bjcp_subcategory_choices = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
            ('E', 'E'), ('F', 'F')) 
    beer = models.ForeignKey(Beer)    
    bottle_date = models.DateField()
    url = models.URLField(verbose_name='URL', blank=True)
    notes = models.TextField(blank=True)
    competition = models.ForeignKey(Competition)
    entry_number = models.IntegerField(blank=True)
    bjcp_category = models.IntegerField(verbose_name='BJCP Category')
    bjcp_subcategory = models.CharField(max_length=1,
            verbose_name='BJCP Subcategory', choices=bjcp_subcategory_choices)
    ordinal_position = models.IntegerField(null=True, blank=True)
    number_in_flight = models.IntegerField(null=True, blank=True)
    final_assigned_score = models.IntegerField(null=True, blank=True)
    place_awarded = models.IntegerField(null=True, blank=True)
    advanced_to_mini_bos = models.BooleanField()

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return u'%s: %s (bottled %s)' % (self.competition, self.beer, self.bottle_date)

class Result(models.Model):
    entry = models.ForeignKey(Entry)
    judge = models.ForeignKey(Judge)
    descriptors = models.ManyToManyField(Descriptor, null=True)

    def __unicode__(self):
        return u'%s, judged by %s' % (self.entry, self.judge)

class Rating(models.Model):
    result = models.ForeignKey(Result)
    rating = models.IntegerField()
    comments = models.TextField(blank=True)
    attribute = models.ForeignKey(Attribute)

    def __unicode__(self):
        return u'%s: %d/%d' % (self.attribute.name, self.rating,
                self.attribute.max_rating)
