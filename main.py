import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        for po in updatable:
            po.update(dt)
        
        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.check_collisions(asteroid):
                    shot.kill()
                    asteroid.split()
                    
        
        screen.fill((0, 0, 0))

        for po in drawable:
            po.draw(screen)

        pygame.display.flip()
        dt = fps.tick(60)/1000


if __name__ == "__main__":
    main()