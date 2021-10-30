# Graphical Interface for Conversion Calculator
import sys
import pygame

# -------------------------------------------------------------------------------------------------
# Utility Functions
def draw_text(text, font, color, surface, x, y):
    '''
    Outputs text at the specified location, using the required parameters
    '''
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# -------------------------------------------------------------------------------------------------
# Main Menu
# #f44336
def menu():
    '''
    Menu function that creates the graphical user interface and controls the program by calling necessary functions
    '''
    pygame.init()
    clock = pygame.time.Clock()
    SCREEN_WIDTH = 1900
    SCREEN_HEIGHT = 980
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Base Conversion Calculator | Asianguy_123')
    title_font = pygame.font.SysFont('corbelb', 100)
    button_font = pygame.font.SysFont('corbelb', 80)
    bg_colour = pygame.Color('#DFDFDF')
    accent_colour = pygame.Color('#3B3D3B')

    header_box = pygame.Rect(0, 0, SCREEN_WIDTH, 140)  
    addition_button = pygame.Rect(1275, 165, 600, 370)
    subtraction_button = pygame.Rect(1275, 585, 600, 370)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

                            
        pygame.draw.line(SCREEN, accent_colour, (SCREEN_WIDTH/2 + 300, 0), (SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT), 4)
        pygame.draw.rect(SCREEN, accent_colour, header_box)
        draw_text('BASE CONVERSION CALCULATOR', title_font, (255, 255, 255), SCREEN, SCREEN_WIDTH/2, 70)
        pygame.draw.rect(SCREEN, pygame.Color('#fff3f3'), addition_button)
        pygame.draw.rect(SCREEN, pygame.Color('#fff3f3'), subtraction_button)
        draw_text('ADDITION', button_font, accent_colour, SCREEN, addition_button.centerx, addition_button.centery)
        draw_text('SUBTRACTION', button_font, accent_colour, SCREEN, subtraction_button.centerx, subtraction_button.centery)

        pygame.display.flip()
        clock.tick(60)
        SCREEN.fill(bg_colour)

if '__main__' == __name__:
    menu()