# Generated by Django 4.0.5 on 2022-06-14 06:34

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('slides', wagtail.blocks.StructBlock([('slides', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False)), ('button_text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('image_text', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=False)), ('image_text', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('left_title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('left_caption', wagtail.blocks.CharBlock(max_length=255, required=False)), ('left_text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('left_button_text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('left_button_page', wagtail.blocks.PageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('right_title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('right_text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('right_caption', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('list', wagtail.blocks.CharBlock(max_length=255, required=False))]))), ('right_button_text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('right_button_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('video_image_text', wagtail.blocks.StructBlock([('video_image_text', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('video', wagtail.blocks.URLBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False)), ('text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('button_text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('services', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=False)), ('services', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('button_text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('menus', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('title_page', wagtail.blocks.PageChooserBlock(required=False)), ('menus', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('left_menu_text', wagtail.blocks.CharBlock(max_length=255, required=False)), ('left_menu_page', wagtail.blocks.PageChooserBlock(required=False)), ('right_menu_text', wagtail.blocks.CharBlock(max_length=255, required=False)), ('right_menu_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('topbar', wagtail.blocks.StructBlock([('topbar', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('menu_text', wagtail.blocks.CharBlock(max_length=255, required=False)), ('menu_page', wagtail.blocks.PageChooserBlock(required=False))]))), ('twitter', wagtail.blocks.URLBlock(max_length=255, required=False)), ('facebook', wagtail.blocks.URLBlock(max_length=255, required=False)), ('instagram', wagtail.blocks.URLBlock(max_length=255, required=False)), ('linkedin', wagtail.blocks.URLBlock(max_length=255, required=False)), ('youtube', wagtail.blocks.URLBlock(max_length=255, required=False))])), ('images', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))])), ('products', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('products', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='', max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('teams', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=False)), ('teams', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.blocks.CharBlock(max_length=255, required=False)), ('designation', wagtail.blocks.CharBlock(max_length=255, required=False)), ('twitter', wagtail.blocks.URLBlock(max_length=255, required=False)), ('facebook', wagtail.blocks.URLBlock(max_length=255, required=False)), ('linkedin', wagtail.blocks.URLBlock(max_length=255, required=False))])))]))], use_json_field=None),
        ),
    ]
