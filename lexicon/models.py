from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Entry(models.Model):
	entry_name = models.CharField(max_length=200)

	def __str__(self):
		return self.entry_name


class Case(models.Model):
	case_entry = models.ForeignKey(Entry, related_name='case')
	case_name = models.CharField(max_length=200)

	NOUN = 'noun'
	VERB = 'verb'
	ADJECTIVE = 'adj'
	ADVERB = 'adv'

	case_function_choices = (
		(NOUN, 'Noun'),
		(VERB, 'Verb'),
		(ADJECTIVE, 'Adjective'),
		(ADVERB, 'Adverb'),
	)

	case_function = models.CharField(max_length=10, choices=case_function_choices, default=NOUN)

	case_definition = models.TextField(default='')
	case_example = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.case_name


class Definition(models.Model):
	definition_case = models.ForeignKey(Case, related_name='definition')
	definition_text = models.TextField()
	definition_example = models.TextField()

	def __str__(self):
		return self.definition_text

