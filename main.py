""" Weather app"""

# modules
import flet
from flet import *
import requests
import datetime


# api_key = '8d3b0a2d8e81b13ba60923d557f702b2'
#
# response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={api_key}')
#
# print(response)

def main(page: flet.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

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
            animate=animation.Animation(duration=350, curve='decelerate'),
            on_hover=lambda e: _expand(e)

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
    flet.app(target=main, assets_dir='assets')
