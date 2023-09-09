# Graphical Interface for Conversion Calculator

# Imports
import sys
import pygame
from conversions import *

# Strange code that doesnt work for some reason that i want to ask about:

# [line 680] 
# if results_bool:
#     output_boxes = [den_out_box, oc_out_box, tc_out_box, sm_out_box, hex_out_box, octal_out_box, bcd_out_box]
#     for result in results:                
#         draw_text(str(result), button_sub_font, accent_colour, SCREEN, output_boxes[results.index(result)].centerx, output_boxes[results.index(result)].centery)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Utility Functions

def draw_text(text, font, color, surface, x, y):
    '''
    Outputs text at the specified location, with (x,y) being the centre of the text object, using the required parameters
    '''

    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Addition Window

def addition():
    '''
    Addition Menu where calculation mode is selected and result is represented in relevant bases
    '''

    # rects to be drawn to make display
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

    # Booleans and base variables
    bases = ['', '']
    mode_selected = False
    input_1_active = False
    input_2_active = False
    multiple_results = None
    base_1_value = ''
    base_2_value = ''
    result = ''
    funcs = [den_add_den, den_add_bin, den_add_hex, bin_add_bin, bin_add_hex, hex_add_hex] # functions to be used
    func = []

    while True:
        # -------------------------------------------------------------------------------------------------
        # Drawing display

        # Drawing GUI frame
        pygame.draw.rect(SCREEN, (255, 255, 255), calculate_button) 
        draw_text('CALCULATE', button_font, accent_colour, SCREEN, calculate_button.centerx, calculate_button.centery)
        pygame.draw.line(SCREEN, accent_colour, (SCREEN_WIDTH/2 + 300, 0), (SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT), 4)
        pygame.draw.rect(SCREEN, accent_colour, header_box)
        draw_text('BASE CONVERSION CALCULATOR', title_font, (255, 255, 255), SCREEN, SCREEN_WIDTH/2, 70)

        # Drawing mode buttons
        pygame.draw.rect(SCREEN, button_colour, den_add_den_button)
        pygame.draw.rect(SCREEN, button_colour, den_add_bin_button)
        pygame.draw.rect(SCREEN, button_colour, den_add_hex_button)
        pygame.draw.rect(SCREEN, button_colour, bin_add_bin_button)
        pygame.draw.rect(SCREEN, button_colour, bin_add_hex_button)
        pygame.draw.rect(SCREEN, button_colour, hex_add_hex_button)

        # Labelling mode buttons
        draw_text('DENARY + DENARY', button_sub_font, accent_colour, SCREEN, den_add_den_button.centerx, den_add_den_button.centery)
        draw_text('DENARY + BINARY', button_sub_font, accent_colour, SCREEN, den_add_bin_button.centerx, den_add_bin_button.centery)
        draw_text('DENARY + HEXADECIMAL', button_sub_font, accent_colour, SCREEN, den_add_hex_button.centerx, den_add_hex_button.centery)
        draw_text('BINARY + BINARY', button_sub_font, accent_colour, SCREEN, bin_add_bin_button.centerx, bin_add_bin_button.centery)
        draw_text('BINARY + HEXADECIMAL', button_sub_font, accent_colour, SCREEN, bin_add_hex_button.centerx, bin_add_hex_button.centery)
        draw_text('HEXADECIMAL + HEXADECIMAL', button_sub_font, accent_colour, SCREEN, hex_add_hex_button.centerx, hex_add_hex_button.centery)

        # Drawing other text and rects
        pygame.draw.rect(SCREEN, button_colour, base_1_box)
        pygame.draw.rect(SCREEN, button_colour, base_2_box)        
        draw_text(base_1_value, button_sub_font, accent_colour, SCREEN, base_1_box.centerx, base_1_box.centery)
        draw_text(base_2_value, button_sub_font, accent_colour, SCREEN, base_2_box.centerx, base_2_box.centery)
        pygame.draw.rect(SCREEN, button_colour, output_box)
        draw_text('Result:', button_sub_font, accent_colour, SCREEN, 1300, 665)

        # -------------------------------------------------------------------------------------------------
        # Button Presses

        mx, my = pygame.mouse.get_pos() # gets mouse co-ordinates

        # Denary add denary selected
        if den_add_den_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Denary']
                func = funcs[0]

        # Denary add binary selected
        if den_add_bin_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Binary']
                func = funcs[1]

        # Denary add hexadecimal selected
        if den_add_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Hex']
                func = funcs[2]

        # Binary add binary selected
        if bin_add_bin_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Binary', 'Binary']
                func = funcs[3]

        # Binary add hexadecimal selected
        if bin_add_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Binary', 'Hex']
                func = funcs[4]

        # Hexadecimal add hexadecimal selected
        if hex_add_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Hex', 'Hex']
                func = funcs[5]
        
        # -------------------------------------------------------------------------------------------------
        # Input + event detection

        # Instructions
        draw_text(f'Enter {bases[0]} value:', button_sub_font, accent_colour, SCREEN, 1350, 275)
        draw_text(f'Enter {bases[1]} value:', button_sub_font, accent_colour, SCREEN, 1350, 365)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # closes GUI if window is closed
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # return to menu if escape pressed
                    menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True # if mouse clicked, click is True

                if event.type == pygame.MOUSEBUTTONDOWN and base_1_box.collidepoint(mx, my): # if input box selected input is active
                    input_1_active = True
                    input_2_active = False
                    base_1_value = ''

                if event.type == pygame.MOUSEBUTTONDOWN and base_2_box.collidepoint(mx, my): # if input box selected input is active
                    input_1_active = False
                    input_2_active = True
                    base_2_value = ''

            if mode_selected:
                if input_1_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            base_1_value = base_1_value[:-1] # deletes character from input
                        else:
                            base_1_value += event.unicode # adds character to input

                if input_2_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            base_2_value = base_2_value[:-1] # deletes character from input
                        else:
                            base_2_value += event.unicode # adds character to input
        
        # -------------------------------------------------------------------------------------------------
        # Calculation

        if calculate_button.collidepoint(mx, my): # if calculate button pressed
            if click:
                result = func(base_1_value, base_2_value) # calls appropriate function and stores result
                if isinstance(result, tuple): # if multi-base addition store as 2 seperate variables
                    result_one = result[0]
                    result_two = result[1]
                    multiple_results = True
                else:
                    multiple_results = False
                
        if multiple_results:
            draw_text(f'{bases[0]}: {result_one}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery - 50) # draws base 1 result
            draw_text(f'{bases[1]}: {result_two}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery + 50) # draws base 2 result

        elif multiple_results == False:
            draw_text(f'{bases[0]}: {result}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery) # draws single result 

        elif multiple_results == None:
            draw_text('', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery) # default blank output box

        # window update
        pygame.display.flip()
        clock.tick(60)
        SCREEN.fill(bg_colour)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Subtraction Window

def subtraction():
    '''
    Subtraction Menu where calculation mode is selected and result is represented in relevant bases
    '''

    # rects to be drawn to make display
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
    base_1_box = pygame.Rect(1254, 290, 648, 60)
    base_2_box = pygame.Rect(1254, 380, 648, 60)
    output_box = pygame.Rect(1254, 680, 648, 300)
    
    # Booleans and base variables
    bases = ['', '']
    mode_selected = False
    input_1_active = False
    input_2_active = False
    multiple_results = None
    base_1_value = ''
    base_2_value = ''
    result = ''
    funcs = [den_sub_den, den_sub_bin, den_sub_hex, bin_sub_bin, bin_sub_den, bin_sub_hex, hex_sub_hex, hex_sub_den, hex_sub_bin] # functions to be used
    func = []

    while True: 
        # -------------------------------------------------------------------------------------------------
        # Drawing display

        # Drawing GUI frame
        pygame.draw.rect(SCREEN, (255, 255, 255), calculate_button) 
        draw_text('CALCULATE', button_font, accent_colour, SCREEN, calculate_button.centerx, calculate_button.centery)
        pygame.draw.line(SCREEN, accent_colour, (SCREEN_WIDTH/2 + 300, 0), (SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT), 4)
        pygame.draw.rect(SCREEN, accent_colour, header_box)
        draw_text('BASE CONVERSION CALCULATOR', title_font, (255, 255, 255), SCREEN, SCREEN_WIDTH/2, 70)

        # Drawing mode buttons
        pygame.draw.rect(SCREEN, button_colour, den_sub_den_button)
        pygame.draw.rect(SCREEN, button_colour, den_sub_bin_button)
        pygame.draw.rect(SCREEN, button_colour, den_sub_hex_button)
        pygame.draw.rect(SCREEN, button_colour, bin_sub_bin_button)
        pygame.draw.rect(SCREEN, button_colour, bin_sub_den_button)
        pygame.draw.rect(SCREEN, button_colour, bin_sub_hex_button)
        pygame.draw.rect(SCREEN, button_colour, hex_sub_hex_button)
        pygame.draw.rect(SCREEN, button_colour, hex_sub_den_button)
        pygame.draw.rect(SCREEN, button_colour, hex_sub_bin_button)

        # Labelling mode buttons
        draw_text('DENARY - DENARY', button_sub_font, accent_colour, SCREEN, den_sub_den_button.centerx, den_sub_den_button.centery)
        draw_text('DENARY - BINARY', button_sub_font, accent_colour, SCREEN, den_sub_bin_button.centerx, den_sub_bin_button.centery)
        draw_text('DENARY - HEXADECIMAL', button_sub_font, accent_colour, SCREEN, den_sub_hex_button.centerx, den_sub_hex_button.centery)
        draw_text('BINARY - BINARY', button_sub_font, accent_colour, SCREEN, bin_sub_bin_button.centerx, bin_sub_bin_button.centery)
        draw_text('BINARY - DENARY', button_sub_font, accent_colour, SCREEN, bin_sub_den_button.centerx, bin_sub_den_button.centery)
        draw_text('BINARY - HEXADECIMAL', button_sub_font, accent_colour, SCREEN, bin_sub_hex_button.centerx, bin_sub_hex_button.centery)
        draw_text('HEXADECIMAL - HEXADECIMAL', button_sub_font, accent_colour, SCREEN, hex_sub_hex_button.centerx, hex_sub_hex_button.centery)
        draw_text('HEXADECIMAL - DENARY', button_sub_font, accent_colour, SCREEN, hex_sub_den_button.centerx, hex_sub_den_button.centery)
        draw_text('HEXADECIMAL - BINARY', button_sub_font, accent_colour, SCREEN, hex_sub_bin_button.centerx, hex_sub_bin_button.centery)

        # Drawing other key text and rects
        pygame.draw.rect(SCREEN, button_colour, base_1_box)
        pygame.draw.rect(SCREEN, button_colour, base_2_box)        
        draw_text(base_1_value, button_sub_font, accent_colour, SCREEN, base_1_box.centerx, base_1_box.centery)
        draw_text(base_2_value, button_sub_font, accent_colour, SCREEN, base_2_box.centerx, base_2_box.centery)
        pygame.draw.rect(SCREEN, button_colour, output_box)
        draw_text('Result:', button_sub_font, accent_colour, SCREEN, 1300, 665)

        # -------------------------------------------------------------------------------------------------
        # Button Presses

        mx, my = pygame.mouse.get_pos() # gets mouse co-ordinates

        # Denary subtract denary selected
        if den_sub_den_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Denary']
                func = funcs[0]

        # Denary subtract binary selected
        if den_sub_bin_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Binary']
                func = funcs[1]

        # Denary subtract hexadecimal selected
        if den_sub_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Denary', 'Hex']
                func = funcs[2]

        # Binary subtract binary selected
        if bin_sub_bin_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Binary', 'Binary']
                func = funcs[3]

        # Binary subtract denary selected
        if bin_sub_den_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Binary', 'Denary']
                func = funcs[4]

        # Binary subtract hexadecimal selected
        if bin_sub_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Binary', 'Hex']
                func = funcs[5]

        # Hexadecimal subtract hexadecimal selected
        if hex_sub_hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Hex', 'Hex']
                func = funcs[6]

        # Hexadecimal subtract denary selected
        if hex_sub_den_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Hex', 'Denary']
                func = funcs[7]

        # Hexadecimal subtract binary selected
        if hex_sub_bin_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                bases = ['Hex', 'Binary']
                func = funcs[8]

        # -------------------------------------------------------------------------------------------------
        # Input + event detection

        # Instructions
        draw_text(f'Enter {bases[0]} value:', button_sub_font, accent_colour, SCREEN, 1350, 275)
        draw_text(f'Enter {bases[1]} value:', button_sub_font, accent_colour, SCREEN, 1350, 365)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # closes GUI if window is closed
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # return to menu if escape pressed
                    menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True # if mouse clicked, click is True

                if event.type == pygame.MOUSEBUTTONDOWN and base_1_box.collidepoint(mx, my): # if input box selected input is active
                    input_1_active = True
                    input_2_active = False
                    base_1_value = ''

                if event.type == pygame.MOUSEBUTTONDOWN and base_2_box.collidepoint(mx, my): # if input box selected input is active
                    input_1_active = False
                    input_2_active = True
                    base_2_value = ''

            if mode_selected:
                if input_1_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            base_1_value = base_1_value[:-1] # deletes character from input
                        else:
                            base_1_value += event.unicode # adds character to input

                if input_2_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            base_2_value = base_2_value[:-1] # deletes character from input
                        else:
                            base_2_value += event.unicode # adds character to input
        
        # -------------------------------------------------------------------------------------------------
        # Calculation

        if calculate_button.collidepoint(mx, my): # if calculate button pressed
            if click:
                result = func(base_1_value, base_2_value) # calls appropriate function and stores result    
                if isinstance(result, tuple): # if multi-base subtraction store as 2 seperate variables
                    result_one = result[0]
                    result_two = result[1]
                    multiple_results = True
                else:
                    multiple_results = False
        
        if multiple_results:
            draw_text(f'{bases[0]}: {result_one}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery - 50) # draws base 1 result
            draw_text(f'{bases[1]}: {result_two}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery + 50) # draws base 2 result

        elif multiple_results == False:
            draw_text(f'{bases[0]}: {result}', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery) # draws single result

        elif multiple_results == None:
            draw_text('', button_sub_font, accent_colour, SCREEN, output_box.centerx, output_box.centery) # default blank output box

        # window update
        pygame.display.flip()
        clock.tick(60)
        SCREEN.fill(bg_colour)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Menu

def menu():
    '''
    Main Menu where conversions take place as well as selecting for addition and subtraction modes
    '''
    
    # rects to be drawn to make display
    addition_button = pygame.Rect(1275, 165, 600, 370)
    subtraction_button = pygame.Rect(1275, 585, 600, 370)
    conversion_button = pygame.Rect(5, 150, 300, 165)
    denary_button = pygame.Rect(5, SCREEN_HEIGHT/3 + 7, 300, 120)
    binary_button = pygame.Rect(5, SCREEN_HEIGHT/3 + 137, 300, 120)
    hex_button = pygame.Rect(5, SCREEN_HEIGHT/3 + 267, 300, 120)
    octal_button = pygame.Rect(5, SCREEN_HEIGHT/3 + 397, 300, 120)
    bcd_button = pygame.Rect(5, SCREEN_HEIGHT/3 + 527, 300, 120)
    input_box = pygame.Rect(325, 150, 913, 165)
    den_out_box = pygame.Rect(325, SCREEN_HEIGHT/3 + 7, 913, 120)
    oc_out_box = pygame.Rect(325, SCREEN_HEIGHT/3 + 137, 913, 35)
    tc_out_box = pygame.Rect(325, SCREEN_HEIGHT/3 + 177, 913, 40)
    sm_out_box = pygame.Rect(325, SCREEN_HEIGHT/3 + 222, 913, 35)
    hex_out_box = pygame.Rect(325, SCREEN_HEIGHT/3 + 267, 913, 120)
    octal_out_box = pygame.Rect(325, SCREEN_HEIGHT/3 + 397, 913, 120)
    bcd_out_box = pygame.Rect(325, SCREEN_HEIGHT/3 + 527, 913, 120)

    # Booleans and base variables
    mode_selected = False
    input_active = False
    input_value = ''
    den_to_x = False
    neg_den_to_x = False
    bin_to_x = False
    neg_bin_to_x = False
    hex_to_x = False
    octal_to_x = False
    bcd_to_x = False
    results = []
    results_bool = False
    click = False

    while True: 
        # -------------------------------------------------------------------------------------------------
        # Drawing display

        # Drawing GUI frame and key buttons
        pygame.draw.line(SCREEN, accent_colour, (SCREEN_WIDTH/2 + 300, 0), (SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT), 4)
        pygame.draw.rect(SCREEN, accent_colour, header_box)
        draw_text('BASE CONVERSION CALCULATOR', title_font, (255, 255, 255), SCREEN, SCREEN_WIDTH/2, 70)
        pygame.draw.rect(SCREEN, button_colour, addition_button)
        pygame.draw.rect(SCREEN, button_colour, subtraction_button)
        draw_text('ADDITION', button_font, accent_colour, SCREEN, addition_button.centerx, addition_button.centery)
        draw_text('Denary - Binary - Hexadecimal', button_sub_font, faint_accent_colour, SCREEN, addition_button.centerx, addition_button.centery + 40)
        draw_text('SUBTRACTION', button_font, accent_colour, SCREEN, subtraction_button.centerx, subtraction_button.centery)
        draw_text('Denary - Binary - Hexadecimal', button_sub_font, faint_accent_colour, SCREEN, subtraction_button.centerx, subtraction_button.centery + 40)
        pygame.draw.line(SCREEN, accent_colour, (0, SCREEN_HEIGHT/3), (1250, SCREEN_HEIGHT/3), 4)
        pygame.draw.line(SCREEN, accent_colour, (315, 140), (315, SCREEN_HEIGHT), 4)
        pygame.draw.rect(SCREEN, (255, 0, 0), conversion_button)
        draw_text('CONVERT', button_font, (255, 255, 255), SCREEN, conversion_button.centerx, conversion_button.centery)

        # Drawing conversion buttons
        pygame.draw.rect(SCREEN, button_colour, denary_button)
        pygame.draw.rect(SCREEN, button_colour, binary_button)
        pygame.draw.rect(SCREEN, button_colour, hex_button)
        pygame.draw.rect(SCREEN, button_colour, octal_button)
        pygame.draw.rect(SCREEN, button_colour, bcd_button)

        # Drawing output boxes
        pygame.draw.rect(SCREEN, bg_colour, den_out_box)
        pygame.draw.rect(SCREEN, bg_colour, oc_out_box)
        pygame.draw.rect(SCREEN, bg_colour, tc_out_box)
        pygame.draw.rect(SCREEN, bg_colour, sm_out_box)
        pygame.draw.rect(SCREEN, bg_colour, hex_out_box)
        pygame.draw.rect(SCREEN, bg_colour, octal_out_box)
        pygame.draw.rect(SCREEN, bg_colour, bcd_out_box)

        # Drawing other lines, text and boxes
        pygame.draw.line(SCREEN, accent_colour, (0, denary_button.bottom + 5), (1248, denary_button.bottom + 5), 3)
        pygame.draw.line(SCREEN, accent_colour, (0, binary_button.bottom + 5), (1248, binary_button.bottom + 5), 3)
        pygame.draw.line(SCREEN, accent_colour, (0, hex_button.bottom + 5), (1248, hex_button.bottom + 5), 3)
        pygame.draw.line(SCREEN, accent_colour, (0, octal_button.bottom + 5), (1248, octal_button.bottom + 5), 3)
        draw_text('DENARY', button_font, accent_colour, SCREEN, denary_button.centerx, denary_button.centery)
        draw_text('BINARY', button_font, accent_colour, SCREEN, binary_button.centerx, binary_button.centery)
        draw_text('Input TC Only', button_sub_font, faint_accent_colour, SCREEN, binary_button.centerx, binary_button.centery + 40)
        draw_text('OC', button_sub_font, faint_accent_colour, SCREEN, binary_button.centerx + 130, binary_button.centery - 40)
        pygame.draw.line(SCREEN, accent_colour, (315, binary_button.centery - 22.5), (1248, binary_button.centery - 22.5), 1)
        pygame.draw.line(SCREEN, accent_colour, (315, binary_button.centery + 22.5), (1248, binary_button.centery + 22.5), 1)
        draw_text('TC', button_sub_font, faint_accent_colour, SCREEN, binary_button.centerx + 130, binary_button.centery)
        draw_text('SM', button_sub_font, faint_accent_colour, SCREEN, binary_button.centerx + 130, binary_button.centery + 40)
        draw_text('HEX', button_font, accent_colour, SCREEN, hex_button.centerx, hex_button.centery)        
        draw_text('OCTAL', button_font, accent_colour, SCREEN, octal_button.centerx, octal_button.centery)
        draw_text('BCD', button_font, accent_colour, SCREEN, bcd_button.centerx, bcd_button.centery)
        pygame.draw.rect(SCREEN, (255, 255, 255), input_box)
        draw_text(input_value, button_font, accent_colour, SCREEN, input_box.centerx, input_box.centery)

        # -------------------------------------------------------------------------------------------------
        # Button Presses

        # Calling addition and subtraction
        mx, my = pygame.mouse.get_pos() # gets mouse co-ordinates
        if addition_button.collidepoint(mx, my):
            if click:
                addition() # calls addition function
        if subtraction_button.collidepoint(mx, my):
            if click:
                subtraction() # calls subtraction function

        # Denary ==> x conversion selected
        if denary_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                den_to_x = True
                neg_den_to_x = False
                bin_to_x = False
                neg_bin_to_x = False
                hex_to_x = False
                octal_to_x = False
                bcd_to_x = False
                results_bool = False

        # Binary ==> x conversion selected
        if binary_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                den_to_x = False
                neg_den_to_x = False
                bin_to_x = True
                neg_bin_to_x = False
                hex_to_x = False
                octal_to_x = False
                bcd_to_x = False
                results_bool = False

        # Hexadecimal ==> x conversion selected
        if hex_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                den_to_x = False
                neg_den_to_x = False
                bin_to_x = False
                neg_bin_to_x = False
                hex_to_x = True
                octal_to_x = False
                bcd_to_x = False
                results_bool = False

        # Octal ==> x conversion selected
        if octal_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                den_to_x = False
                neg_den_to_x = False
                bin_to_x = False
                neg_bin_to_x = False
                hex_to_x = False
                octal_to_x = True
                bcd_to_x = False
                results_bool = False

        # Binary Coded Decimal ==> x conversion selected
        if bcd_button.collidepoint(mx, my):
            if click:
                mode_selected = True
                den_to_x = False
                neg_den_to_x = False
                bin_to_x = False
                neg_bin_to_x = False
                hex_to_x = False
                octal_to_x = False
                bcd_to_x = True
                results_bool = False
        
        # -------------------------------------------------------------------------------------------------
        # Input + event detection

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # closes GUI if window is closed
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True # if mouse clicks, click is true

                if event.type == pygame.MOUSEBUTTONDOWN and input_box.collidepoint(mx, my): # if input box clicked input can be entered
                    input_active = True
                    input_value = ''

            if mode_selected:
                if input_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            input_value = input_value[:-1] # deletes character from input
                        else:
                            input_value += event.unicode # adds character to inout
                
        # -------------------------------------------------------------------------------------------------
        # Conversion

        if conversion_button.collidepoint(mx, my): # if convert  button is pressed
            if click:    
                if den_to_x:
                    results = []
                    if int(input_value) < 0: 
                        neg_den_to_x = True # entered value is negative

                    # conversions necessary for negative denary
                    if neg_den_to_x:
                        results.extend([input_value, neg_den_to_ones_comp_bin(input_value), neg_den_to_twos_comp_bin(input_value), den_to_sm_bin(input_value), '', '', ''])
                    # conversions necessary for positive denary
                    else:
                        results.extend([input_value, '', '', den_to_sm_bin(input_value), den_to_n_base(input_value, 16), den_to_n_base(input_value, 8), den_to_bcd(input_value)])
                    results_bool = True

                if bin_to_x:
                    results = []
                    if input_value[0] == '1':
                        neg_bin_to_x = True # entered value is negative

                    # conversions necessary for negative binary
                    if neg_bin_to_x:
                        results.extend([twos_comp_bin_to_neg_den(input_value), twos_comp_to_ones_comp(input_value), input_value, twos_comp_to_sm_bin(input_value), '', '', ''])
                    # conversions necessary for positive binary
                    else:
                        results.extend([bin_to_den(input_value), '', input_value, input_value, bin_to_hex(input_value), bin_to_octal(input_value), bin_to_bcd(input_value)])
                    results_bool = True

                if hex_to_x:
                    results = []
                    # conversions necessary for hexadecimal
                    results.extend([hex_to_den(input_value), '', '', hex_to_bin(input_value), input_value, hex_to_octal(input_value), hex_to_bcd(input_value)])
                    results_bool = True

                if octal_to_x:
                    results = []
                    # conversions necessary for octal
                    results.extend([octal_to_den(input_value), '', '', octal_to_bin(input_value), octal_to_hex(input_value), input_value, octal_to_bcd(input_value)])
                    results_bool = True

                if bcd_to_x:
                    results = []
                    # conversions necessary for binary coded decimal
                    results.extend([bcd_to_den(input_value), '', '', bcd_to_bin(input_value), bcd_to_hex(input_value), bcd_to_octal(input_value), input_value])
                    results_bool = True

        # outputs converted values
        if results_bool:           
            draw_text(str(results[0]), button_sub_font, accent_colour, SCREEN, den_out_box.centerx, den_out_box.centery)
            draw_text(str(results[1]), button_sub_font, accent_colour, SCREEN, oc_out_box.centerx, oc_out_box.centery)
            draw_text(str(results[2]), button_sub_font, accent_colour, SCREEN, tc_out_box.centerx, tc_out_box.centery)
            draw_text(str(results[3]), button_sub_font, accent_colour, SCREEN, sm_out_box.centerx, sm_out_box.centery)
            draw_text(str(results[4]), button_sub_font, accent_colour, SCREEN, hex_out_box.centerx, hex_out_box.centery)
            draw_text(str(results[5]), button_sub_font, accent_colour, SCREEN, octal_out_box.centerx, octal_out_box.centery)
            draw_text(str(results[6]), button_sub_font, accent_colour, SCREEN, bcd_out_box.centerx, bcd_out_box.centery)
            
            # sets all booleans back to false
            den_to_x = False
            neg_den_to_x = False
            bin_to_x = False
            neg_bin_to_x = False
            hex_to_x = False
            octal_to_x = False
            bcd_to_x = False

        # window update
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
pygame.display.set_caption('Base Conversion Calculator | Sunain Syed')
title_font = pygame.font.SysFont('corbelb', 100)
button_font = pygame.font.SysFont('corbelb', 80)
button_sub_font = pygame.font.SysFont('corbelb', 30)
bg_colour = pygame.Color('#E1E1E1')
accent_colour = pygame.Color('#3B3D3B')
faint_accent_colour = pygame.Color('#A2A3A2')
button_colour = pygame.Color('#fff3f3')
header_box = pygame.Rect(0, 0, SCREEN_WIDTH, 140)

# -------------------------------------------------------------------------------------------------
# Runs program

if '__main__' == __name__:
    menu()
