from wagtail.core.blocks import (CharBlock, ListBlock, PageChooserBlock,
                                 StructBlock, TextBlock, URLBlock)
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


class ImageTextBlock(StructBlock):
    heading = CharBlock(max_length=255, required=False)
    image_text = ListBlock(StructBlock(
        [
            ("left_title", CharBlock(max_length=255, required=False)),
            ("left_caption", CharBlock(max_length=255, required=False)),
            ("left_text", TextBlock(max_length=255, required=False)),
            ("left_button_text", TextBlock(max_length=255, required=False)),
            ("left_button_page", PageChooserBlock(required=False)),

            ("image", ImageChooserBlock(required=False)),

            ("right_title", CharBlock(max_length=255, required=False)),
            ("right_text", TextBlock(max_length=255, required=False)),
            ("right_caption", ListBlock(StructBlock(
                [("list", CharBlock(max_length=255, required=False))]))),
            ("right_button_text", TextBlock(max_length=255, required=False)),
            ("right_button_page", PageChooserBlock(required=False)),
        ]
    ))

    class Meta:
        template = "blocks/image_text_block.html"


class VideoImageTextBlock(StructBlock):
    video_image_text = ListBlock(StructBlock(
        [
            ("video", URLBlock(max_length=255, required=False)),
            ("image", ImageChooserBlock(required=False)),

            ("title", CharBlock(max_length=255, required=False)),
            ("caption", CharBlock(max_length=255, required=False)),
            ("text", TextBlock(max_length=255, required=False)),
            ("button_text", TextBlock(max_length=255, required=False)),
            ("button_page", PageChooserBlock(required=False))
        ]
    ))

    class Meta:
        template = "blocks/video_image_text_block.html"
