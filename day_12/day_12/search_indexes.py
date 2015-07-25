from haystack import indexes
from day_12.models import *

class LanguageIndex(indexes.SearchIndex,indexes.Indexable):
	text=indexes.CharField(document=True, use_template=True)
	lang_name=indexes.CharField(model_attr='lang_name',faceted=True)
	score=indexes.CharField(model_attr='score',faceted=True)

	def get_model(self):
		return lang

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
