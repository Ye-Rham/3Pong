import pygame
from pygame.sprite import Sprite


class MidPaddle1(Sprite):
    def __init__(self, settings, screen):
        super(MidPaddle1, self).__init__()
        self.screen = screen
        self.width = settings.vertical_paddle_width
        self.height = settings.vertical_paddle_height
        self.color = settings.paddle1_color
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.center = float(self.rect.centery)

        self.speed = settings.vertical_paddle_speed
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.speed

        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.speed

        self.rect.centery = self.center

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_paddle(self):
        self.center = self.screen_rect.centery
        self.rect.centery = self.center


class TopPaddle1(Sprite):
    def __init__(self, settings, screen):
        super(TopPaddle1, self).__init__()
        self.screen = screen
        self.width = settings.horizontal_paddle_width
        self.height = settings.horizontal_paddle_height
        self.color = settings.paddle1_color
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx/2
        self.rect.top = self.screen_rect.top
        self.center = float(self.rect.centerx)

        self.speed = settings.horizontal_paddle_speed
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.speed

        elif self.moving_right and self.rect.right < self.screen_rect.centerx:
            self.center += self.speed

        self.rect.centerx = self.center

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_paddle(self):
        self.center = self.screen_rect.centerx/2
        self.rect.centerx = self.center


class BottomPaddle1(Sprite):
    def __init__(self, settings, screen):
        super(BottomPaddle1, self).__init__()
        self.screen = screen
        self.width = settings.horizontal_paddle_width
        self.height = settings.horizontal_paddle_height
        self.color = settings.paddle1_color
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx/2
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.speed = settings.horizontal_paddle_speed
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.speed

        elif self.moving_right and self.rect.right < self.screen_rect.centerx:
            self.center += self.speed

        self.rect.centerx = self.center

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_paddle(self):
        self.center = self.screen_rect.centerx/2
        self.rect.centerx = self.center


class MidPaddle2(Sprite):
    def __init__(self, settings, screen):
        super(MidPaddle2, self).__init__()
        self.screen = screen
        self.width = settings.vertical_paddle_width
        self.height = settings.vertical_paddle_height
        self.color = settings.paddle2_color
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        self.center = float(self.rect.centery)

        self.speed = settings.vertical_paddle_speed
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.speed

        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.speed

        self.rect.centery = self.center

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_paddle(self):
        self.center = self.screen_rect.centery
        self.rect.centery = self.center


class TopPaddle2(Sprite):
    def __init__(self, settings, screen):
        super(TopPaddle2, self).__init__()
        self.screen = screen
        self.width = settings.horizontal_paddle_width
        self.height = settings.horizontal_paddle_height
        self.color = settings.paddle2_color
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx * 1.5
        self.rect.top = self.screen_rect.top
        self.center = float(self.rect.centerx)

        self.speed = settings.horizontal_paddle_speed
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left and self.rect.left > self.screen_rect.centerx:
            self.center -= self.speed

        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed

        self.rect.centerx = self.center

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_paddle(self):
        self.center = self.screen_rect.centerx * 1.5
        self.rect.centerx = self.center


class BottomPaddle2(Sprite):
    def __init__(self, settings, screen):
        super(BottomPaddle2, self).__init__()
        self.screen = screen
        self.width = settings.horizontal_paddle_width
        self.height = settings.horizontal_paddle_height
        self.color = settings.paddle2_color
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx * 1.5
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.speed = settings.horizontal_paddle_speed
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left and self.rect.left > self.screen_rect.centerx:
            self.center -= self.speed

        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed

        self.rect.centerx = self.center

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_paddle(self):
        self.center = self.screen_rect.centerx * 1.5
        self.rect.centerx = self.center
