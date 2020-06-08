import pygame

class GameClient():
    def __str__(self):
        pygame.init()

        self.win = pygame.display.set_mode((1280, 720))

        pygame.display.set_caption("Chess Game created by michaeldsim")
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.running = True
        win.fill((166, 238, 133))
        pygame.display.update()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.quitGame()

    def quitGame(self):
        pygame.quit()
        quit()

# TODO: still messing around with pygame and learning it
# I have no idea what I am doing lol