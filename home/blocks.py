from wagtail.core.blocks import (CharBlock, ListBlock, PageChooserBlock,
                                 StructBlock, TextBlock)
from wagtail.images.blocks import ImageChooserBlock


class SlideBlock(StructBlock):
    slides = ListBlock(StructBlock(
        [
            ("title", CharBlock(max_length=255, required=False)),
            ("image", ImageChooserBlock(required=False)),
            ("caption", CharBlock(max_length=255, required=False)),
            ("button_text", TextBlock(max_length=255, required=False)),
            ("button_page", PageChooserBlock(required=False))
        ]
    ))

    class Meta:
        template = "blocks/slides_block.html"
