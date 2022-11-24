import pygame


class EndScreen:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((600, 450))
        pygame.display.set_caption('Overtale')
        
        self.display_screen()
        
    def display_screen(self) -> None:
        #Display end screen
        pass

    def restart_button(self) -> None:
        pass

    def quit_button(self) -> None:

    