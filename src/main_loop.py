import os

import pygame
from collections import defaultdict


class MainLoop:
    """Window initialization and the main loop

    This class created to separate game-logic from mainloop. Its run method does all basic pygame stuff:
    handle events, update game status, and draw sprites to main_surface.
    """
    def __init__(self, caption, screen_size, frame_rate):
        self.running = True

        pygame.init()
        self.main_surface = pygame.display.set_mode(screen_size)
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{0},{0}"
        pygame.display.set_caption(caption)

        self.frame_rate = frame_rate
        self.clock = pygame.time.Clock()

        self.visible_sprites = pygame.sprite.LayeredUpdates()

        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def update(self):
        """Update game state"""
        self.visible_sprites.update()

    def draw(self):
        """Draw all sprites into screen"""
        self.visible_sprites.draw(self.main_surface)

    def handle_events(self):
        """Handle the player's inputs

        self.keydown_handlers, self.keyup_handlers, and self.mouse_handlers contain objects key (and mouse) handlers.
        So every time then we need out object to respond to player input, we need to add a handle_event method to its
        class and then add this handler to handlers containers.

        When game_handler capture an event it calls the conforming object handle method from self.keyup_handlers,
        self.keydown_handlers, or self.mouse_handlers with key as an argument in case of keyup-keydown event or
        mouse position with mouse button in case of mouse event.

        Then the object can update its state in reply to transmitted event (key, mouse move, or mouse button).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def add_up_down_key_handlers(self, obj, key):
        self.keydown_handlers[key].append(obj.handle_key_down)
        self.keyup_handlers[key].append(obj.handle_key_up)

    def run(self):
        while self.running:

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
