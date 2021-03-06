# Generated by Django 3.2.11 on 2022-01-17 10:48

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('HeroImage', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Title', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(help_text='Entre your image'))])), ('FeaturesItems', wagtail.core.blocks.StructBlock([('feature_item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Title', required=False)), ('description', wagtail.core.blocks.TextBlock(default='RichText', required=False))])))]))]),
        ),
    ]
