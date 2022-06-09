from wagtail.core.blocks import (CharBlock, ListBlock, StructBlock, TextBlock,
                                 URLBlock)
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    cards = ListBlock(StructBlock(
        [
            ("title", CharBlock(max_length=255, required=False)),
            ("image", ImageChooserBlock(required=False)),
            ("caption", CharBlock(max_length=255, required=False)),
            ("button_text", TextBlock(max_length=255, required=False)),
            ("button_url", URLBlock(required=False))
        ]
    ))

    class Meta:
        template = "blocks/image_block.html"