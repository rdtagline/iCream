from django.db import models
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel, PageChooserPanel)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


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


class MenuItem(Orderable):

    link_title = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=255, blank=True, null=True)
    link_page = models.ForeignKey(
        "wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL)
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'


@register_snippet
class Menu(ClusterableModel):

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")
    ]

    def __str__(self):
        return self.title


@register_setting
class LogoSettings(BaseSetting):
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, blank=True, null=True)

    panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel("image")
            ], heading="Logo Settings"
        )
    ]
