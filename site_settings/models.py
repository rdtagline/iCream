from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class FooterSettings(BaseSetting):
    heading = models.CharField(max_length=255, blank=True, null=True)
    related_page = models.ForeignKey(
        'wagtailcore.Page', on_delete=models.SET_NULL, blank=True, null=True)
    left_title = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    right_title = models.CharField(max_length=255, blank=True, null=True)
    opening = models.TextField(max_length=255, blank=True, null=True)
    closing = models.TextField(max_length=255, blank=True, null=True)

    domain_name = models.CharField(max_length=255, blank=True, null=True)
    domain_text = models.TextField(max_length=255, blank=True, null=True)

    designer_name = models.CharField(max_length=255, blank=True, null=True)
    designer_url = models.URLField(max_length=255, blank=True, null=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("heading"),
                FieldPanel("related_page"),
                FieldPanel("left_title"),
                FieldPanel("address"),
                FieldPanel("phone"),
                FieldPanel("right_title"),
                FieldPanel("opening"),
                FieldPanel("closing"),

                FieldPanel("domain_name"),
                FieldPanel("domain_text"),

                FieldPanel("designer_name"),
                FieldPanel("designer_url"),
            ], heading="Footer Settings"
        )
    ]


@register_setting
class SocialMediaSettings(BaseSetting):
    twitter = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter"),
                FieldPanel("facebook"),
                FieldPanel("linkedin"),
                FieldPanel("instagram"),
                FieldPanel("youtube"),
            ], heading="Social Media Settings"
        )
    ]
