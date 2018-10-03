import pygame.font


class Score1:
    def __init__(self, screen):
        super(Score1, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.text_color = (50, 50, 50)
        self.font = pygame.font.SysFont(None, 300)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx, self.rect.centery = self.screen_rect.centerx/2, self.screen_rect.centery

        self.msg_image = None
        self.msg_image_rect = None

        self.points = 0
        self.prep_msg(str(self.points))

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, (0, 0, 0))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Score2:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.text_color = (50, 50, 50)
        self.font = pygame.font.SysFont(None, 300)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx, self.rect.centery = self.screen_rect.centerx*1.5, self.screen_rect.centery

        self.msg_image = None
        self.msg_image_rect = None

        self.points = 0
        self.prep_msg(str(self.points))

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, (0, 0, 0))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Winner:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (150, 150, 150)
        self.font = pygame.font.SysFont(None, 200)

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.center = self.screen_rect.center

        self.msg_image = None
        self.msg_image_rect = None

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, (0, 0, 0))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
