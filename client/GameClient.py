import pygame


def quit_game():
    pygame.quit()
    quit()


class GameClient:
    def __init__(self):
        pygame.init()

        self.win = pygame.display.set_mode((1280, 720))

        pygame.display.set_caption("Chess Game created by michaeldsim")
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.running = True
        self.win.fill((166, 238, 133))
        pygame.display.update()
        clock = pygame.time.Clock()
        while self.running:
            # This is the game loop
            # dt is how you can ensure everything moves at the same speed regardless of the computer
            # you use this and multiply by speed to ensure same speed on any fps
            dt = clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    quit_game()


client = GameClient()

# TODO: still messing around with pygame and learning it
# I have no idea what I am doing lol
