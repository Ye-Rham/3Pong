import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, settings, screen):
        self.screen = screen
        self.width = settings.ball_width
        self.height = settings.ball_height
        self.color = settings.ball_color
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.rise = settings.ball_rise
        self.run = settings.ball_run
        self.speed = settings.ball_speed

    def update(self):
        self.centery += self.rise * self.speed
        self.centerx += self.run * self.speed
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    def reset_ball(self, settings):
        self.rise = settings.ball_rise
        self.run = settings.ball_run
        self.speed = settings.ball_speed
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery