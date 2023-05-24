import csv
from index_calculator.models import Taxon, Genus, Family, Order, Class

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


class InsensitiveDictReader(csv.DictReader):
    # This class overrides the csv.fieldnames property, which converts all fieldnames without leading and trailing spaces and to lower case.
    @property
    def fieldnames(self):
        return [field.strip().lower() for field in csv.DictReader.fieldnames.fget(self)]
    def next(self):
        return InsensitiveDict(csv.DictReader.__next__(self))
class InsensitiveDict(dict):
    # This class overrides the __getitem__ method to automatically strip() and lower() the input key
    def __getitem__(self, key):
        return dict.__getitem__(self, key.strip().lower())


# def bmwp(csv_file):
#     bmwp_score = 0
#     ancylidae = ['ancylus fluviatilis', 'ancylus sp.', 'ancylidae',
#                  'ancylidae/acroloxidae', '"ancylidae" gen. sp.']
#
#     for row in csv.DictReader(csv_file):
#         try:
#             taxon = Taxon.objects.get(taxon=row['taxon'])
#         except ObjectDoesNotExist:
#             messages.error(request, f"{row['taxon']} is not a valid taxon name!")
#         else:
#             if taxon.classs.classs.lower() == "oligochaeta":
#                 bmwp_score += taxon.classs.bmwp_score
#             elif row['taxon'].lower() in ancylidae:
#                 bmwp_score += 6
#             else:
#                 bmwp_score += taxon.family.bmwp_score
#
#     return bmwp_score
