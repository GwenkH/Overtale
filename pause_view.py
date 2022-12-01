# import pygame
# # from pygame.constants import KEYDOWN, K_p, K_q
# from game.base_view import BaseView
# from game.overtale import Overtale

# class PauseView(BaseView):
#     def __init__(self, parent: BaseView) -> None:
#         self. parent = parent
    
#     def event_loop(self, events) -> None:
#         for event in events:
#             if event.type == pygame.locals.KEYDOWN:
#                 if event.key == K_p:
#                     Overtale.set_current_view(self.parent)
#                 elif event.key == K_q:
#                     from game.main_menu import MainMenu
#                     Overtale.set_current_view(MainMenu())
    
#     def update(self) -> None:
#         pass

#     def draw(self, surface: pygame.Surface) -> None:
#         self.parent.draw(surface)