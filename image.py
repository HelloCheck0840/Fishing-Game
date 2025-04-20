import pygame

BASE_PATH = 'image/'

def load_image(path, size, rotation):
    image = pygame.image.load(BASE_PATH + path).convert()
    image.set_colorkey((0, 0, 0))
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, rotation)
    return image

def load_image_alpha(path, size, rotation):
    image = pygame.image.load(BASE_PATH + path).convert_alpha()
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, rotation)
    return image

def draw_surface(size, color):
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(color)
    return surf