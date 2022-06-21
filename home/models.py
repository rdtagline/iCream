from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.fields import RichTextField, StreamField
from wagtail.models import Page

from .blocks import *


class HomePage(Page):
    template = "home/home_page.html"
    content = StreamField(
        [
            ('slides', SlideBlock()),
            ('image_text', ImageTextBlock()),
            ('video_image_text', VideoImageTextBlock()),
            ('services', ServiceBlock()),
            ('images', ImageBlock()),
            ('products', ProductBlock()),
            ("teams", TeamMemberBlock()),
            ("clients", ClientBlock()),
            ("about_page", AboutPageBlock()),
            ("products_page", ProductPageBlock()),
            ("gallery_page", GalleryPageBlock()),
        ], blank=True, null=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):

    template = "home/contact_page.html"
    landing_page_template = "home/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]
