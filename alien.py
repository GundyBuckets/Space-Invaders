import pygame, random

# Alien class represents an alien sprite in the game
class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.type = type
        # Load the image for the alien based on its type
        path = f"Graphics/alien_{type}.png"
        self.image = pygame.image.load(path)
        # Set the position of the alien
        self.rect = self.image.get_rect(topleft=(x, y))

    # Update the position of the alien based on the direction
    def update(self, direction):
        self.rect.x += direction

# MysteryShip class represents a mystery ship sprite in the game
class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width, offset):
        super().__init__()
        self.screen_width = screen_width
        self.offset = offset
        # Load the image for the mystery ship
        self.image = pygame.image.load("Graphics/mystery.png")

        # Randomly choose the starting position (left or right edge of the screen)
        x = random.choice([self.offset / 2, screen_width + self.offset - self.image.get_width()])
        if x == self.offset / 2:
            self.speed = 3  # Move to the right
        else:
            self.speed = -3  # Move to the left
        
        # Set the position of the mystery ship
        self.rect = self.image.get_rect(topleft=(x, 90))

    # Update the position of the mystery ship
    def update(self):
        self.rect.x += self.speed
        # Remove the ship if it moves off the screen
        if self.rect.right > self.screen_width + self.offset / 2:
            self.kill()
        elif self.rect.left < self.offset / 2:
            self.kill()