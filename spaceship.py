import pygame
from laser import Laser

# Spaceship class represents the player's spaceship in the game
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, offset):
        super().__init__()
        self.offset = offset
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Load the image for the spaceship
        self.image = pygame.image.load("Graphics/spaceship.png")
        # Set the position of the spaceship
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height))
        self.speed = 6
        # Group to hold all the lasers fired by the spaceship
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 300
        self.laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")

    # Get user input to control the spaceship
    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False
            self.laser_time = pygame.time.get_ticks()
            # Create a new laser and add it to the group
            laser = Laser(self.rect.center, 5, self.screen_height)
            self.lasers_group.add(laser)
            self.laser_sound.play()

    # Update the spaceship's state
    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()

    # Constrain the spaceship's movement within the screen boundaries
    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

        if self.rect.left < self.offset:
            self.rect.left = self.offset

    # Recharge the laser to allow firing again after a delay
    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    # Reset the spaceship to its initial position and state
    def reset(self):
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height))
        self.lasers_group.empty()