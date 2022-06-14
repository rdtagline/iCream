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


class ServiceBlock(StructBlock):
    heading = CharBlock(max_length=255, required=False)
    services = ListBlock(StructBlock(
        [
            ("image", ImageChooserBlock(required=False)),
            ("title", CharBlock(max_length=255, required=False)),
            ("text", TextBlock(max_length=255, required=False)),
            ("button_text", TextBlock(max_length=255, required=False)),
            ("button_page", PageChooserBlock(required=False))
        ]
    ))

    class Meta:
        template = "blocks/services_block.html"


class MenuBlock(StructBlock):
    title = CharBlock(max_length=255, required=False)
    title_page = PageChooserBlock(required=False)
    menus = ListBlock(StructBlock(
        [
            ("left_menu_text", CharBlock(max_length=255, required=False)),
            ("left_menu_page", PageChooserBlock(required=False)),
            ("right_menu_text", CharBlock(max_length=255, required=False)),
            ("right_menu_page", PageChooserBlock(required=False)),
        ]
    ))

    class Meta:
        template = "blocks/menu_block.html"


class TopbarBlock(StructBlock):
    topbar = ListBlock(StructBlock(
        [
            ("menu_text", CharBlock(max_length=255, required=False)),
            ("menu_page", PageChooserBlock(required=False))
        ]
    ))
    twitter = URLBlock(max_length=255, required=False)
    facebook = URLBlock(max_length=255, required=False)
    instagram = URLBlock(max_length=255, required=False)
    linkedin = URLBlock(max_length=255, required=False)
    youtube = URLBlock(max_length=255, required=False)

    class Meta:
        template = "blocks/topbar_block.html"


class ImageBlock(StructBlock):
    title = CharBlock(max_length=255, required=False)
    images = ListBlock(StructBlock(
        [
            ("image", ImageChooserBlock(required=False))
        ]
    ))

    class Meta:
        template = "blocks/images_block.html"


class ProductBlock(StructBlock):
    title = CharBlock(max_length=255, required=False)
    products = ListBlock(StructBlock(
        [
            ("title", CharBlock(max_length=255, required=False, help_text="")),
            ("caption", CharBlock(max_length=255, required=False)),
            ("image", ImageChooserBlock(required=False)),
            ("button_text", TextBlock(max_length=255, required=False)),
            ("button_page", PageChooserBlock(required=False)),
        ]
    ))

    class Meta:
        template = "blocks/products_block.html"


class TeamMemberBlock(StructBlock):
    title = CharBlock(max_length=255, required=False)
    teams = ListBlock(StructBlock(
        [
            ("image", ImageChooserBlock(required=False)),
            ("name", CharBlock(max_length=255, required=False)),
            ("designation", CharBlock(max_length=255, required=False)),
            ("twitter", URLBlock(max_length=255, required=False)),
            ("facebook", URLBlock(max_length=255, required=False)),
            ("linkedin", URLBlock(max_length=255, required=False)),
        ]
    ))

    class Meta:
        template = "blocks/team_member_block.html"


class ClientBlock(StructBlock):
    title = CharBlock(max_length=255, required=False)
    clients = ListBlock(StructBlock(
        [
            ("name", CharBlock(max_length=255, required=False)),
            ("profession", CharBlock(max_length=255, required=False)),
            ("text", TextBlock(max_length=255, required=False)),
            ("image", ImageChooserBlock(required=False)),
        ]
    ))

    class Meta:
        template = "blocks/client_block.html"


class FooterBlock(StructBlock):
    heading = CharBlock(max_length=255, required=False)
    heading_page = PageChooserBlock(required=False)
    footer = ListBlock(StructBlock(
        [
            ("left_title", CharBlock(max_length=255, required=False)),
            ("address", TextBlock(max_length=255, required=False)),
            ("phone", TextBlock(max_length=255, required=False)),
            ("right_title", CharBlock(max_length=255, required=False)),
            ("opening", TextBlock(max_length=255, required=False)),
            ("closing", TextBlock(max_length=255, required=False)),

            ("twitter", URLBlock(max_length=255, required=False)),
            ("facebook", URLBlock(max_length=255, required=False)),
            ("linkedin", URLBlock(max_length=255, required=False)),
            ("instagram", URLBlock(max_length=255, required=False)),

            ("domain_name", CharBlock(max_length=255, required=False)),
            ("domain_page", PageChooserBlock(required=False)),
            ("domain_text", TextBlock(max_length=255, required=False)),
            ("designer_name", CharBlock(max_length=255, required=False)),
            ("designer_url", URLBlock(max_length=255, required=False)),
        ]
    ))

    class Meta:
        template = "blocks/footer_block.html"
