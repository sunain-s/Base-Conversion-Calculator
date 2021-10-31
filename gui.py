# Graphical Interface for Conversion Calculator
import sys
import pygame
import conversions
from conversions import *

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
    base_1_box = pygame.Rect(1254, 290, 648, 60)
    base_2_box = pygame.Rect(1254, 380, 648, 60)
    output_box = pygame.Rect(1254, 680, 648, 300)
    bases = ['', '']
    mode_selected = False
    input_1_active = False
    input_2_active = False
    multiple_results = None
    base_1_value = ''
    base_2_value = ''
    result = ''
    funcs = [den_add_den, den_add_bin, den_add_hex, bin_add_bin, bin_add_hex, hex_add_hex]
    func = []
    while True:

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
        pygame.draw.rect(SCREEN, button_colour, base_1_box)
        pygame.draw.rect(SCREEN, button_colour, base_2_box)        
        draw_text(base_1_value, button_sub_font, accent_colour, SCREEN, base_1_box.centerx, base_1_box.centery)
        draw_text(base_2_value, button_sub_font, accent_colour, SCREEN, base_2_box.centerx, base_2_box.centery)
        pygame.draw.rect(SCREEN, button_colour, output_box)
        draw_text('Result:', button_sub_font, accent_colour, SCREEN, 1300, 665)

        mx, my = pygame.mouse.get_pos()
        if den_add_den_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Denary']
                func = funcs[0]
        if den_add_bin_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Binary']
                func = funcs[1]
        if den_add_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Hex']
                func = funcs[2]
        if bin_add_bin_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Binary', 'Binary']
                func = funcs[3]
        if bin_add_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Binary', 'Hex']
                func = funcs[4]
        if hex_add_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Hex', 'Hex']
                func = funcs[5]

        draw_text(f'Enter {bases[0]} value:', button_sub_font, accent_colour, SCREEN, 1350, 275)
        draw_text(f'Enter {bases[1]} value:', button_sub_font, accent_colour, SCREEN, 1350, 365)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if event.type == pygame.MOUSEBUTTONDOWN and base_1_box.collidepoint(mx, my):
                    input_1_active = True
                    input_2_active = False
                    base_1_value = ''
                if event.type == pygame.MOUSEBUTTONDOWN and base_2_box.collidepoint(mx, my):
                    input_1_active = False
                    input_2_active = True
                    base_2_value = ''
            if mode_selected:
                if input_1_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            base_1_value = base_1_value[:-1]
                        else:
                            base_1_value += event.unicode
                if input_2_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            base_2_value = base_2_value[:-1]
                        else:
                            base_2_value += event.unicode 
        
        if calculate_button.collidepoint(mx, my):
            if click:
                result = func(base_1_value, base_2_value)
                if isinstance(result, tuple):
                    result_one = result[0]
                    result_two = result[1]
                    multiple_results = True
                else:
                    multiple_results = False
                
        
        if multiple_results:
            draw_text(f'{bases[0]}: {result_one}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery - 50)
            draw_text(f'{bases[1]}: {result_two}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery + 50)
        elif multiple_results == False:
            draw_text(f'{bases[0]}: {result}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery)
        elif multiple_results == None:
            draw_text('', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery)




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