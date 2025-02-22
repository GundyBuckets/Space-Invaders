import pygame

# Laser class represents a laser sprite in the game
class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__()
        # Create a 4x15 surface for the laser
        self.image = pygame.Surface((4, 15))
        # Fill the laser with a color
        self.image.fill((243, 216, 63))
        # Set the position of the laser
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.screen_height = screen_height

    # Update the position of the laser
    def update(self):
        self.rect.y -= self.speed
        # Remove the laser if it moves off the screen
        if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
            self.kill()
