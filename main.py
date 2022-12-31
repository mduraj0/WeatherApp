""" Weather app"""

# modules
import flet
from flet import *
import requests
import datetime

api_key = '8d3b0a2d8e81b13ba60923d557f702b2'

response = requests.get(f'https://api.openweathermap.org/geo/1.0/reverse?lat=52.21&lon=21.0&limit=5&appid={api_key}')


def main(page: flet.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # animation
    def _expand(e):
        if e.data == 'true':
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.4
            _c.content.controls[0].update()

    def _top():
        top = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=['lightblue600', 'lightblue900']
            ),
            border_radius=35,
            animate=animation.Animation(duration=450, curve='decelerate'),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment='center',
                        controls=[
                            Text(
                                'Warsaw, PL',
                                size=16,
                                weight='w500',
                            )
                        ]
                    ),
                    Container(padding=padding.only
                    (bottom=5)),
                    Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src='./assets/images.png'
                                    ),
                                ]
                            ),
                        ],
                    ),
                ],
            ),

        )

        return top

    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Stack(
            width=300,
            height=550,
            controls=[
                _top()
            ]
        ),
    )

    page.add(_c)


if __name__ == '__main__':
    flet.app(target=main, assets_dir='')
