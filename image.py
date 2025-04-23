import pygame

BASE_PATH = 'image/'

def load_image(path):
    image = pygame.image.load(BASE_PATH + path).convert()
    image.set_colorkey((0, 0, 0))
    return image

def rect_load_image(path):
    image = load_image(path)
    image_rect = image.get_rect()
    return image, image_rect

def load_image_alpha(path):
    image = pygame.image.load(BASE_PATH + path).convert_alpha()
    return image

def draw_surface(size, color):
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(color)
    return surf