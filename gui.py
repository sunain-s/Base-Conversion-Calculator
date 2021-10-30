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
# Addition Window

def addition():
    den_add_den_button = pygame.Rect(15, 160, 605, 260)
    den_add_bin_button = pygame.Rect(15, 430, 605, 260)
    den_add_hex_button = pygame.Rect(15, 700, 605, 260)
    bin_add_bin_button = pygame.Rect(630, 160, 605, 260)
    bin_add_hex_button = pygame.Rect(630, 430, 605, 260)
    hex_add_hex_button = pygame.Rect(630, 700, 605, 260)
    calculate_button = pygame.Rect(1250, 160, 650, 100)
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.draw.rect(SCREEN, (255, 255, 255), calculate_button) 
        draw_text('CALCULATE', button_font, accent_colour, SCREEN, calculate_button.centerx, calculate_button.centery)
        pygame.draw.line(SCREEN, accent_colour, (SCREEN_WIDTH/2 + 300, 0), (SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT), 4)
        pygame.draw.rect(SCREEN, accent_colour, header_box)
        draw_text('BASE CONVERSION CALCULATOR', title_font, (255, 255, 255), SCREEN, SCREEN_WIDTH/2, 70)
        pygame.draw.rect(SCREEN, button_colour, den_add_den_button)
        pygame.draw.rect(SCREEN, button_colour, den_add_bin_button)
        pygame.draw.rect(SCREEN, button_colour, den_add_hex_button)
        pygame.draw.rect(SCREEN, button_colour, bin_add_bin_button)
        pygame.draw.rect(SCREEN, button_colour, bin_add_hex_button)
        pygame.draw.rect(SCREEN, button_colour, hex_add_hex_button)
        draw_text('DENARY + DENARY', button_sub_font, accent_colour, SCREEN, den_add_den_button.centerx, den_add_den_button.centery)
        draw_text('DENARY + BINARY', button_sub_font, accent_colour, SCREEN, den_add_bin_button.centerx, den_add_bin_button.centery)
        draw_text('DENARY + HEXADECIMAL', button_sub_font, accent_colour, SCREEN, den_add_hex_button.centerx, den_add_hex_button.centery)
        draw_text('BINARY + BINARY', button_sub_font, accent_colour, SCREEN, bin_add_bin_button.centerx, bin_add_bin_button.centery)
        draw_text('BINARY + HEXADECIMAL', button_sub_font, accent_colour, SCREEN, bin_add_hex_button.centerx, bin_add_hex_button.centery)
        draw_text('HEXADECIMAL + HEXADECIMAL', button_sub_font, accent_colour, SCREEN, hex_add_hex_button.centerx, hex_add_hex_button.centery)
        
        


        pygame.display.flip()
        clock.tick(60)
        SCREEN.fill(bg_colour)

# -------------------------------------------------------------------------------------------------
# Subtraction Window

def subtraction():
    den_sub_den_button = pygame.Rect(10, 160, 400, 260)
    den_sub_bin_button = pygame.Rect(10, 430, 400, 260)
    den_sub_hex_button = pygame.Rect(10, 700, 400, 260)
    bin_sub_bin_button = pygame.Rect(425, 160, 400, 260)
    bin_sub_den_button = pygame.Rect(425, 430, 400, 260)
    bin_sub_hex_button = pygame.Rect(425, 700, 400, 260)
    hex_sub_hex_button = pygame.Rect(840, 160, 400, 260)
    hex_sub_den_button = pygame.Rect(840, 430, 400, 260)
    hex_sub_bin_button = pygame.Rect(840, 700, 400, 260)
    calculate_button = pygame.Rect(1250, 160, 650, 100)


    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.draw.rect(SCREEN, (255, 255, 255), calculate_button) 
        draw_text('CALCULATE', button_font, accent_colour, SCREEN, calculate_button.centerx, calculate_button.centery)
        pygame.draw.line(SCREEN, accent_colour, (SCREEN_WIDTH/2 + 300, 0), (SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT), 4)
        pygame.draw.rect(SCREEN, accent_colour, header_box)
        draw_text('BASE CONVERSION CALCULATOR', title_font, (255, 255, 255), SCREEN, SCREEN_WIDTH/2, 70)
        pygame.draw.rect(SCREEN, button_colour, den_sub_den_button)
        pygame.draw.rect(SCREEN, button_colour, den_sub_bin_button)
        pygame.draw.rect(SCREEN, button_colour, den_sub_hex_button)
        pygame.draw.rect(SCREEN, button_colour, bin_sub_bin_button)
        pygame.draw.rect(SCREEN, button_colour, bin_sub_den_button)
        pygame.draw.rect(SCREEN, button_colour, bin_sub_hex_button)
        pygame.draw.rect(SCREEN, button_colour, hex_sub_hex_button)
        pygame.draw.rect(SCREEN, button_colour, hex_sub_den_button)
        pygame.draw.rect(SCREEN, button_colour, hex_sub_bin_button)
        draw_text('DENARY - DENARY', button_sub_font, accent_colour, SCREEN, den_sub_den_button.centerx, den_sub_den_button.centery)
        draw_text('DENARY - BINARY', button_sub_font, accent_colour, SCREEN, den_sub_bin_button.centerx, den_sub_bin_button.centery)
        draw_text('DENARY - HEXADECIMAL', button_sub_font, accent_colour, SCREEN, den_sub_hex_button.centerx, den_sub_hex_button.centery)
        draw_text('BINARY - BINARY', button_sub_font, accent_colour, SCREEN, bin_sub_bin_button.centerx, bin_sub_bin_button.centery)
        draw_text('BINARY - DENARY', button_sub_font, accent_colour, SCREEN, bin_sub_den_button.centerx, bin_sub_den_button.centery)
        draw_text('BINARY - HEXADECIMAL', button_sub_font, accent_colour, SCREEN, bin_sub_hex_button.centerx, bin_sub_hex_button.centery)
        draw_text('HEXADECIMAL - HEXADECIMAL', button_sub_font, accent_colour, SCREEN, hex_sub_hex_button.centerx, hex_sub_hex_button.centery)
        draw_text('HEXADECIMAL - DENARY', button_sub_font, accent_colour, SCREEN, hex_sub_den_button.centerx, hex_sub_den_button.centery)
        draw_text('HEXADECIMAL - BINARY', button_sub_font, accent_colour, SCREEN, hex_sub_bin_button.centerx, hex_sub_bin_button.centery)

        pygame.display.flip()
        clock.tick(60)
        SCREEN.fill(bg_colour)

# -------------------------------------------------------------------------------------------------
# Main Menu

def menu():
    '''
    Main Menu where conversions take place as well as 
    '''
    

      
    addition_button = pygame.Rect(1275, 165, 600, 370)
    subtraction_button = pygame.Rect(1275, 585, 600, 370)
    
    while True:
        click = False
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
        pygame.draw.rect(SCREEN, button_colour, addition_button)
        pygame.draw.rect(SCREEN, button_colour, subtraction_button)
        draw_text('ADDITION', button_font, accent_colour, SCREEN, addition_button.centerx, addition_button.centery)
        draw_text('Denary - Binary - Hexadecimal', button_sub_font, faint_accent_colour, SCREEN, addition_button.centerx, addition_button.centery + 40)
        draw_text('SUBTRACTION', button_font, accent_colour, SCREEN, subtraction_button.centerx, subtraction_button.centery)
        draw_text('Denary - Binary - Hexadecimal', button_sub_font, faint_accent_colour, SCREEN, subtraction_button.centerx, subtraction_button.centery + 40)

        mx, my = pygame.mouse.get_pos()
        if addition_button.collidepoint(mx, my):
            if click:
                addition()
        if subtraction_button.collidepoint(mx, my):
            if click:
                subtraction()


        pygame.display.flip()
        clock.tick(60)
        SCREEN.fill(bg_colour)

# -------------------------------------------------------------------------------------------------
# Constants

pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 980
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Base Conversion Calculator | Asianguy_123')
title_font = pygame.font.SysFont('corbelb', 100)
button_font = pygame.font.SysFont('corbelb', 80)
button_sub_font = pygame.font.SysFont('corbelb', 30)
bg_colour = pygame.Color('#DFDFDF')
accent_colour = pygame.Color('#3B3D3B')
faint_accent_colour = pygame.Color('#A2A3A2')
button_colour = pygame.Color('#fff3f3')
header_box = pygame.Rect(0, 0, SCREEN_WIDTH, 140)

# -------------------------------------------------------------------------------------------------

if '__main__' == __name__:
    menu()
