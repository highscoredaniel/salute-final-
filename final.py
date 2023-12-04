import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Movement")

# Clock to control the frame rate
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")  # Replace with your spritesheet image path
        self.rect = self.image.get_rect()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % 5  # Change 5 to the number of frames in your spritesheet
            self.image = self.get_image(self.frame_index)

    def get_image(self, frame):
        frame_width = self.rect.width / 5  # Change 5 to the number of frames in your spritesheet
        frame_height = self.rect.height
        rect = pygame.Rect(frame * frame_width, 0, frame_width, frame_height)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.image, (0, 0), rect)
        image.set_colorkey(WHITE)
        return image

# Create sprite groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
