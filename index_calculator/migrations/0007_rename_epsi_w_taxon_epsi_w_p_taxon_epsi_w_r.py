# Generated by Django 4.1.3 on 2023-02-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "index_calculator",
            "0006_subfamily_family_dehli_dis_genus_dehli_dis_tribe_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="taxon",
            old_name="epsi_w",
            new_name="epsi_w_p",
        ),
        migrations.AddField(
            model_name="taxon",
            name="epsi_w_r",
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
