from abc import ABC, abstractmethod
import pygame, sys
from pygame.locals import QUIT
from game.base_view import BaseView


class BaseGame(ABC):
    game: 'BaseGame' = None

    def __init__(self) -> None:
        """init"""
        BaseGame.game = self

        #Initializing Pygame
        pygame.init()

        #Screen
        width = 600
        height = 450
        size = (width, height)
        self.screen = pygame.display.set_mode(size)
        self.current_view: BaseView = None
        # pygame.display.set_caption('Overtale')

        self.create()

        # clock
        self.clock = pygame.time.Clock()
    
    @staticmethod
    def set_current_view(view: BaseView) -> None:
        BaseGame.game.current_view = view

    @abstractmethod
    def create(self) -> None: ...

    def run(self) -> None:
        run = True
        while run:     
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        pygame.quit()
                        sys.exit()

            
            # --
            self.current_view.event_loop(events)
            self.current_view.update()
            self.current_view.draw(self.screen)



            pygame.display.update()
            self.clock.tick(60)
    pygame.quit()

