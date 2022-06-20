from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.core.fields import StreamField
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
        ]
    )
    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]
