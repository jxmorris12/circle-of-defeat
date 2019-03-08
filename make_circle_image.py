from game import Game
from PIL import Image, ImageDraw, ImageFont
from math import sin, cos, pi

_font = ImageFont.truetype("Arial", 16)

def show_game_circle(games):

        # Therefore a circle with a center (150 * 7.5, 100 * 7.5) and radius of 100 * 7.5 will embed
        # itself nicely into the center. We can traverse this circle at intervals of 2pi/15,
        # placing one of the logos at each step.

    background = Image.new('RGBA', (120 * 15, 100 * 15), (255, 255, 255, 255))
    w, h = background.size

    for n in range(len(games)):
        game = games[n]
        team = game.winning_team()

        img = Image.open('./logos/{}.gif'.format(team), 'r')
        img_w, img_h = img.size

        # Insert image onto background
        RADIUS = 100 * 7.5 * 0.65
        x = sin(n * 2 * pi / len(games)) * RADIUS + w / 2
        y = cos(n * 2 * pi / len(games)) * RADIUS + h / 2
        offset = (int(x - img_w / 2), int(y - img_h / 2))
        background.paste(img, offset)

        # Add text
        draw = ImageDraw.Draw(background)
        T_RADIUS = 1.2 * RADIUS
        tx = sin(n * 2 * pi / len(games)) * T_RADIUS + w / 2
        ty = cos(n * 2 * pi / len(games)) * T_RADIUS + h / 2

        text = '{} beat {}\non {}'.format(
            game.winning_team(),
            game.losing_team(),
            game.date())

        tw, th = _font.getsize(text)

        tx -= tw / 2
        ty -= th / 2

        # draw.text((tx, ty),text,(0,0,0),font=_font)
    background.save('out2.png')
