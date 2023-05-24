import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator


class Class(models.Model):
    classis = models.CharField(max_length=50,
                               help_text="Class the taxon belongs to.")
    furse_code = models.CharField(max_length=8)

    def __str__(self):
        return self.classis


class Subclass(models.Model):
    subclassis = models.CharField(max_length=50,
                                  help_text="Subclass the taxon belongs to.")
    bmwp_score = models.IntegerField(validators=[MinValueValidator(1),
                                                 MaxValueValidator(10)],
                                     null=True)
    whpt_ab1 = models.FloatField(verbose_name="Abundance level 1", null=True)
    whpt_ab2 = models.FloatField(verbose_name="Abundance level 2", null=True)
    whpt_ab3 = models.FloatField(verbose_name="Abundance level 3", null=True)
    whpt_ab4 = models.FloatField(verbose_name="Abundance level 4", null=True)
    whpt_po = models.FloatField(verbose_name="Values for estimating WHPT from "
                                             "data without abundance information",
                                null=True)
    classis = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subclassis


class Order(models.Model):
    ordo = models.CharField(max_length=50,
                            help_text="Order the taxon belongs to.")
    furse_code = models.CharField(max_length=8, null=True)
    subclassis = models.ForeignKey('Subclass', on_delete=models.SET_NULL, null=True)
    classis = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ordo


class Family(models.Model):
    familia = models.CharField(max_length=50,
                               help_text="Family the taxon belongs to.")
    furse_code = models.CharField(max_length=8, null=True)
    bmwp_score = models.IntegerField(validators=[MinValueValidator(1),
                                                 MaxValueValidator(10)],
                                     null=True)
    whpt_ab1 = models.FloatField(verbose_name="Abundance level 1", null=True)
    whpt_ab2 = models.FloatField(verbose_name="Abundance level 2", null=True)
    whpt_ab3 = models.FloatField(verbose_name="Abundance level 3", null=True)
    whpt_ab4 = models.FloatField(verbose_name="Abundance level 4", null=True)
    whpt_po = models.FloatField(verbose_name="Values for estimating WHPT from "
                                             "data without abundance information",
                                null=True)
    life_fg = models.CharField(max_length=2,
                               help_text="Flow group value",
                               null=True)
    psi_fssr = models.CharField(max_length=1,
                                help_text="Fine Sediment Sensitivity Rating group",
                                null=True)
    dehli_dis = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(10)],
                                    null=True)
    ordo = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    subclassis = models.ForeignKey('Subclass', on_delete=models.SET_NULL, null=True)
    classis = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.familia


class Subfamily(models.Model):
    subfamilia = models.CharField(max_length=50,
                                  help_text="Subfamily the taxon belongs to.")
    dehli_dis = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(10)],
                                    null=True)
    familia = models.ForeignKey('Family', on_delete=models.SET_NULL, null=True)
    ordo = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    subclassis = models.ForeignKey('Subclass', on_delete=models.SET_NULL, null=True)
    classis = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)


class Tribe(models.Model):
    tribus = models.CharField(max_length=50,
                              help_text="Tribe the taxon belongs to.")
    dehli_dis = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(10)],
                                    null=True)
    subfamilia = models.ForeignKey('Subfamily', on_delete=models.SET_NULL, null=True)
    familia = models.ForeignKey('Family', on_delete=models.SET_NULL, null=True)
    ordo = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    subclassis = models.ForeignKey('Subclass', on_delete=models.SET_NULL, null=True)
    classis = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)


class Genus(models.Model):
    genus = models.CharField(max_length=50,
                             help_text="Genus the taxon belongs to.")
    furse_code = models.CharField(max_length=8, null=True)
    dehli_dis = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(10)],
                                    null=True)
    tribus = models.ForeignKey('Tribe', on_delete=models.SET_NULL, null=True)
    subfamilia = models.ForeignKey('Subfamily', on_delete=models.SET_NULL, null=True)
    familia = models.ForeignKey('Family', on_delete=models.SET_NULL, null=True)
    ordo = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    subclassis = models.ForeignKey('Subclass', on_delete=models.SET_NULL, null=True)
    classis = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.genus


# BWMP score values are within the Family model/table
class Taxon(models.Model):
    taxon = models.CharField(max_length=100,
                             help_text="Name of the taxon.")
    furse_code = models.CharField(max_length=8, null=True)
    authority = models.CharField(max_length=70, null=True,
                                 verbose_name="Author(s) and year when the "
                                              "taxon was first described.")
    psi_fssr = models.CharField(max_length=1, null=True)
    epsi_w_r = models.FloatField(null=True)
    epsi_w_p = models.FloatField(null=True)
    life_fg = models.CharField(max_length=2,
                               help_text="Flow group value",
                               null=True)
    cci_cs = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(10)],
                                 null=True)
    dehli_dis = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(10)],
                                    null=True)
    bmwp_score = models.IntegerField(validators=[MinValueValidator(1),
                                                 MaxValueValidator(10)],
                                     null=True)
    genus = models.ForeignKey('Genus', on_delete=models.SET_NULL, null=True)
    tribus = models.ForeignKey('Tribe', on_delete=models.SET_NULL, null=True)
    subfamilia = models.ForeignKey('Subfamily', on_delete=models.SET_NULL, null=True)
    familia = models.ForeignKey('Family', on_delete=models.SET_NULL, null=True)
    ordo = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    subclassis = models.ForeignKey('Subclass', on_delete=models.SET_NULL, null=True)
    classis = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.taxon


class LifeScores(models.Model):
    flow_group = models.CharField(max_length=2,
                                  help_text="Flow group value",
                                  null=True)
    fg_definition = models.CharField(max_length=50,
                                     help_text="Flow group definition",
                                     null=True)
    a_cat_a = models.IntegerField(validators=[MinValueValidator(4),
                                              MaxValueValidator(9)],
                                  help_text="Abundance category - A")
    a_cat_b = models.IntegerField(validators=[MinValueValidator(3),
                                              MaxValueValidator(10)],
                                  help_text="Abundance category - B")
    a_cat_c = models.IntegerField(validators=[MinValueValidator(2),
                                              MaxValueValidator(11)],
                                  help_text="Abundance category - C")
    a_cat_de = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(12)],
                                   help_text="Abundance categories - D/E")


class PsiScores(models.Model):
    fssr_group = models.CharField(max_length=1,
                                  help_text="Fine Sediment Sensitivity Rating group",
                                  null=True)
    fssr_definition = models.CharField(max_length=50,
                                       help_text="Fine Sediment Sensitivity Rating definition",
                                       null=True)
    a_cat_a = models.IntegerField(validators=[MinValueValidator(1),
                                              MaxValueValidator(2)],
                                  help_text="Abundance category - A")
    a_cat_b = models.IntegerField(validators=[MinValueValidator(2),
                                              MaxValueValidator(3)],
                                  help_text="Abundance category - B")
    a_cat_c = models.IntegerField(validators=[MinValueValidator(3),
                                              MaxValueValidator(3)],
                                  help_text="Abundance category - C")
    a_cat_d = models.IntegerField(validators=[MinValueValidator(4),
                                              MaxValueValidator(5)],
                                  help_text="Abundance category - D")
