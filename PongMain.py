import pygame

from GameSettings import Settings
from StartScreen import Title
from StartScreen import Button
from Paddles import MidPaddle1
from Paddles import TopPaddle1
from Paddles import BottomPaddle1
from Paddles import MidPaddle2
from Paddles import TopPaddle2
from Paddles import BottomPaddle2
from Ball import Ball
from Score import Score1
from Score import Score2

import GameFunctions as gf

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("3 Pong")

    play_button = Button(screen, "Play")
    title = Title(screen, "3 PONG")

    midpaddle1 = MidPaddle1(settings, screen)
    toppaddle1 = TopPaddle1(settings, screen)
    bottompaddle1 = BottomPaddle1(settings, screen)
    midpaddle2 = MidPaddle2(settings, screen)
    toppaddle2 = TopPaddle2(settings, screen)
    bottompaddle2 = BottomPaddle2(settings, screen)
    ball = Ball(settings, screen)
    score1 = Score1(screen)
    score2 = Score2(screen)

    title.draw()
    play_button.draw()
    pygame.display.flip()

    while settings.game_start == False:
        gf.check_events(settings, play_button, midpaddle1, toppaddle1, bottompaddle1)

    pygame.mouse.set_visible(False)

    while True:
        gf.check_events(settings, play_button, midpaddle1, toppaddle1, bottompaddle1)
        gf.ai_directives(ball, midpaddle2, toppaddle2, bottompaddle2,)
        gf.check_score(settings, screen, ball, midpaddle1, toppaddle1, bottompaddle1,\
                       midpaddle2, toppaddle2, bottompaddle2, score1, score2)
        gf.update_screen(screen, settings, ball, midpaddle1, toppaddle1, bottompaddle1,\
                         midpaddle2, toppaddle2, bottompaddle2, score1, score2)

run_game()