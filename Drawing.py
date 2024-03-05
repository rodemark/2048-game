import pygame
import sys

from GameField import GameField


class Drawing:
    def __init__(self, game_field):
        pygame.init()
        self.game_field = game_field
        self.tile_size = 100
        self.margin = 10
        self.screen_size = (self.game_field.size * (self.tile_size + self.margin) + self.margin,
                            self.game_field.size * (self.tile_size + self.margin) + self.margin)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('2048 Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 40)

    def draw(self):
        self.screen.fill((187, 173, 160))
        for i in range(self.game_field.size):
            for j in range(self.game_field.size):
                tile_value = self.game_field.grid[i][j]
                if tile_value != 0:
                    pygame.draw.rect(self.screen, TILE_COLORS.get(tile_value, (205, 193, 180)),
                                     (j * (self.tile_size + self.margin) + self.margin,
                                      i * (self.tile_size + self.margin) + self.margin,
                                      self.tile_size, self.tile_size))
                    text = self.font.render(str(tile_value), True, (0, 0, 0))
                    text_rect = text.get_rect(
                        center=(j * (self.tile_size + self.margin) + self.tile_size / 2 + self.margin,
                                i * (self.tile_size + self.margin) + self.tile_size / 2 + self.margin))
                    self.screen.blit(text, text_rect)

        pygame.display.flip()

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.game_field.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.game_field.move_down()
                    elif event.key == pygame.K_LEFT:
                        self.game_field.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.game_field.move_right()
                    if self.game_field.is_game_over():
                        print("Game Over!")
                self.draw()
                self.clock.tick(10)

        pygame.quit()

TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}