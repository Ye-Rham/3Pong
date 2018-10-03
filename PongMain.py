import pygame
from time import sleep

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
from Score import Winner

import GameFunctions as gf


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("PONG: AI - NO WALLS")

    play_button = Button(screen, "Play")
    title = Title(screen, "PONG", 0)
    title2 = Title(screen, "AI - NO WALLS", 50)

    while True:
        screen.fill(settings.bg_color)
        title.draw()
        title2.draw()
        play_button.draw()
        pygame.display.flip()
        midpaddle1 = MidPaddle1(settings, screen)
        toppaddle1 = TopPaddle1(settings, screen)
        bottompaddle1 = BottomPaddle1(settings, screen)
        midpaddle2 = MidPaddle2(settings, screen)
        toppaddle2 = TopPaddle2(settings, screen)
        bottompaddle2 = BottomPaddle2(settings, screen)
        ball = Ball(settings, screen)
        score1 = Score1(screen)
        score2 = Score2(screen)
        winner = Winner(screen)

        while settings.game_start is False:
            gf.check_events(settings, play_button, midpaddle1, toppaddle1, bottompaddle1)

        pygame.mouse.set_visible(False)

        gf.update_screen(screen, settings, ball, midpaddle1, toppaddle1, bottompaddle1,
                         midpaddle2, toppaddle2, bottompaddle2, score1, score2)
        sleep(3)

        while score1.points < 15 and score2.points < 15:
            gf.check_events(settings, play_button, midpaddle1, toppaddle1, bottompaddle1)
            gf.ai_directives(ball, midpaddle2, toppaddle2, bottompaddle2,)
            gf.check_score(settings, screen, ball, midpaddle1, toppaddle1, bottompaddle1,
                           midpaddle2, toppaddle2, bottompaddle2, score1, score2)
            gf.update_game(settings, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2,
                           bottompaddle2)
            gf.update_screen(screen, settings, ball, midpaddle1, toppaddle1, bottompaddle1,
                             midpaddle2, toppaddle2, bottompaddle2, score1, score2)

        if score1.points == 15:
            winner.prep_msg("Player wins!")
            winner.draw()
        else:
            winner.prep_msg("CPU wins!")
            winner.draw()
        pygame.display.flip()
        sleep(3)
        settings.game_start = False
        pygame.mouse.set_visible(True)


run_game()
