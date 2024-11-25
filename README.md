# Extended `social` plugin of `mkdocs-material`

**Enhance your social cards with ease!**

This plugin extends the functionality of the `social` plugin in `mkdocs-material`, allowing for greater customization and support for additional social media platforms. Perfect for creating visually appealing and highly configurable cards for your documentation site.

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/hmasdev/mkdocs-material-extended-social-plugin?sort=semver)
![GitHub Liecense](https://img.shields.io/github/license/hmasdev/mkdocs-material-extended-social-plugin)
![GitHub last commit](https://img.shields.io/github/last-commit/hmasdev/mkdocs-material-extended-social-plugin)

## Requirements

- Python >= 3.10
- Material for MkDocs >= 9.5.45

## How to Use

### Installation

```bash
pip install git+https://github.com/hmasdev/mkdocs-material-extended-social-plugin
```

### Configuration

Add the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - extendedsocial:
```

The configuration schema of `extendedsocial` is same as that of `social` plugin of `mkdocs-material` except for `extra_cards_options`.

Below is the schema of `extra_cards_options`, which serves as the default configuration for `extendedsocial`:

```yaml
plugins:
  - extendedsocial:
      extra_cards_options:
        card_size:
          - 1200
          - 630
        # specify background_image
        background_image: cardbackground.png
        background_image_resize_strategy: keep_aspect_ratio # or resize # keep_aspect_ratio is recommended
        # size of site_name, title, and description
        site_name_size:
          - 826
          - 48
        title_size:
            - 826
            - 328
        description_size:
            - 826
            - 80
        # font size of site_name, title, and description
        site_name_font_size: 36
        title_font_size: 92
        description_font_size: 28
        # maximum number of lines of site_name, title, and description
        site_name_line_max: 1
        title_line_max: 3
        description_line_max: 2
        # line space of site_name, title, and description
        site_name_line_space: 20
        title_line_space: 30
        description_line_space: 14
        # positions
        logo_position_left_top:
            - 972
            - 60
        background_image_position_left_top:
            - 0
            - 0
        site_name_position_left_top:
            - 68
            - 64
        title_position_left_top:
            - 64
            - 160
        description_position_left_top:
            - 68
            - 512
```

You can specify the font size, the maximum number of lines, the line space, and the position of title, description, and site name in the card.

## How to Develop

TBD

## License

- [MIT](LICENSE)

## Author

- [hmasdev](https://github.com/hmasdev)

## Acknowledgements

- [MkDocs](https://www.mkdocs.org/)
  - [(repo)MkDocs](https://github.com/mkdocs/mkdocs)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
  - [(repo) mkdocs-material](https://github.com/squidfunk/mkdocs-material)
