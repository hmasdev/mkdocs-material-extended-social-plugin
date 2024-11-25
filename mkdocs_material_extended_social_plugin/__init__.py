import os
from typing import Literal, TypedDict
from PIL import Image
from mkdocs.config.config_options import Type
from material.plugins.social.plugin import BasePlugin, SocialConfig, SocialPlugin  # type: ignore # noqa


class ExtraSocialConfig(TypedDict):
    # ignore_cache: bool  # TODO: Implement cache control

    card_size: tuple[int, int]
    background_image: str
    background_image_resize_strategy: Literal['resize', 'keep_aspect_ratio']  # noqa

    site_name_size: tuple[int, int]
    title_size: tuple[int, int]
    description_size: tuple[int, int]

    site_name_font_size: int
    title_font_size: int
    description_font_size: int

    site_name_line_max: int
    title_line_max: int
    description_line_max: int

    site_name_line_space: int
    title_line_space: int
    description_line_space: int

    logo_position_left_top: tuple[int, int]
    background_image_position_left_top: tuple[int, int]
    site_name_position_left_top: tuple[int, int]
    title_position_left_top: tuple[int, int]
    description_position_left_top: tuple[int, int]

    @classmethod
    def get_default(cls) -> 'ExtraSocialConfig':
        return ExtraSocialConfig(
            card_size=(1200, 630),
            background_image='',
            background_image_resize_strategy='keep_aspect_ratio',
            site_name_size=(826, 48),
            title_size=(826, 328),
            description_size=(826, 80),
            site_name_font_size=36,
            title_font_size=92,
            description_font_size=28,
            site_name_line_max=1,
            title_line_max=3,
            description_line_max=2,
            site_name_line_space=20,
            title_line_space=30,
            description_line_space=14,
            logo_position_left_top=(1200 - 228, 64 - 4),
            background_image_position_left_top=(0, 0),
            site_name_position_left_top=(64 + 4, 64),
            title_position_left_top=(64, 160),
            description_position_left_top=(64 + 4, 512),
        )


class ExtendedSocialConfig(SocialConfig):
    extra_cards_options = Type(dict, default=dict())


class ExtendedSocialPlugin(BasePlugin[ExtendedSocialConfig], SocialPlugin):

    def on_config(self, config) -> None:
        super().on_config(config)
        if not self.config.cards:
            return
        self.extra_cards_option = (
            ExtraSocialConfig.get_default()
            | ExtraSocialConfig(**config.plugins['extendedsocial'].config['extra_cards_options'])
        )

    def _render_card(
        self,
        site_name: str,
        title: str,
        description: str,
    ) -> Image.Image:
        # Render background and logo
        image = self._render_card_background(
            self.extra_cards_option['card_size'],
            self.color["fill"],
        )
        if os.path.exists(self.extra_cards_option['background_image']):
            bg = Image.open(self.extra_cards_option['background_image']).convert("RGBA")  # noqa
            image.alpha_composite(
                _resize_image(bg, image.size, self.extra_cards_option['background_image_resize_strategy']),  # noqa
                self.extra_cards_option['background_image_position_left_top'],
            )
        image.alpha_composite(
            self._resized_logo_promise.result(),
            self.extra_cards_option['logo_position_left_top'],
        )

        # Render site name
        image.alpha_composite(
            self._render_text(
                self.extra_cards_option["site_name_size"],
                self._get_font(
                    "Bold",
                    self.extra_cards_option['site_name_font_size'],
                ),
                site_name,
                self.extra_cards_option["site_name_line_max"],
                self.extra_cards_option["site_name_line_space"],
            ),
            self.extra_cards_option["site_name_position_left_top"],
        )

        # Render page title
        image.alpha_composite(
            self._render_text(
                self.extra_cards_option['title_size'],
                self._get_font(
                    "Bold",
                    self.extra_cards_option['title_font_size'],
                ),
                title,
                self.extra_cards_option['title_line_max'],
                self.extra_cards_option['title_line_space'],
            ),
            self.extra_cards_option['title_position_left_top'],
        )

        # Render page description
        image.alpha_composite(
            self._render_text(
                self.extra_cards_option['description_size'],
                self._get_font(
                    "Regular",
                    self.extra_cards_option['description_font_size'],
                ),
                description,
                self.extra_cards_option['description_line_max'],
                self.extra_cards_option['description_line_space'],
            ),
            self.extra_cards_option['description_position_left_top'],
        )

        # Return social card image
        return image


def _resize_image(
    image: Image.Image,
    size: tuple[int, int],
    strategy: Literal['resize', 'keep_aspect_ratio'],
) -> Image.Image:
    if strategy == 'resize':
        return image.resize(size)
    if strategy == 'keep_aspect_ratio':
        image.thumbnail(size)
        return image
    raise NotImplementedError(f"Unknown resize strategy: {strategy}")
