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
            ('abouts', AboutBlock())
        ]
    )
    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]
