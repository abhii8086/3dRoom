import pygame
import sys

# to initialize Pygame
pygame.init()

# constants 
SW = 800
SH = 800
RS = 100  # 100x100 sqft. room Size
OBJECT_SIZE = 10  # movable box(object)

# for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# for screen setup
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("3D Room Object Movement")

# initial position of object
obj_position = [SW // 2, SH // 2]

#draw room object
def draw_room():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (0, 0, RS, RS), 1)
    pygame.draw.rect(screen, RED, (obj_position[0], obj_position[1], OBJECT_SIZE, OBJECT_SIZE))
    pygame.display.flip()

# Main loop
def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            obj_position[0] -= 5
        if keys[pygame.K_RIGHT]:
            obj_position[0] += 5
        if keys[pygame.K_UP]:
            obj_position[1] -= 5
        if keys[pygame.K_DOWN]:
            obj_position[1] += 5
            
        # Boundaries that object within the room
        obj_position[0] = max(0, min(RS - OBJECT_SIZE, obj_position[0]))
        obj_position[1] = max(0, min(RS - OBJECT_SIZE, obj_position[1]))
        
        draw_room()
        clock.tick(30)

if __name__ == "__main__":
    main()
