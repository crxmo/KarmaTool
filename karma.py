import os
import time

def resize_console_windows_in_pixels(width_px, height_px, char_width=7, char_height=15):
    # Calculer les colonnes et lignes nécessaires
    cols = width_px // char_width
    lines = height_px // char_height

    # Redimensionner la console
    os.system(f'mode con: cols={cols} lines={lines}')

# Exemple d'utilisation
resize_console_windows_in_pixels(822, 580)

def get_color_gradient(start_color, end_color, steps):
    gradient = []
    for i in range(steps):
        ratio = i / (steps - 1)
        red = int(start_color[0] + ratio * (end_color[0] - start_color[0]))
        green = int(start_color[1] + ratio * (end_color[1] - start_color[1]))
        blue = int(start_color[2] + ratio * (end_color[2] - start_color[2]))
        gradient.append(f'\033[38;2;{red};{green};{blue}m')
    return gradient

def fore_to_rgb(fore_color):
    colors = {
        'RED': (255, 0, 0),
        'LIME': (50, 205, 50),
        'BLUE': (0, 0, 255),
        'PURPLE': (138, 43, 226),
        'PINK': (255, 105, 180),
        'ORANGE': (255, 165, 0),
    }
    return colors.get(fore_color, (255, 0, 0))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    theme_color_name = 'RED'
    theme_rgb = fore_to_rgb(theme_color_name)
    ascii_art_text = r"""
                                    :::!~!!!!!:.
                                .xUHWH!! !!?M88WHX:.
                              .X*#M@$!!  !X!M$$$$$$WWx:.
                             :!!!!!!?H! :!$!$$$$$$$$$$8X:
                            !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                           :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                           ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                            !:~~~  .:!M"T#$$$$WX??#MRRMMM!
                             ~?WuxiW*   "#$$$$8!!!!??!!!
                           :X- M$$$$       "T#$T~!8$WUXU~
                         :%  ~#$$$m:        ~!~ ?$$$$$$
                        :!.-   ~T$$$$8xx.  .xWW- ~""##*"
              .....   -~~:< !    ~?T#$$@@W@*?$$      /
              W$@@M!!! .!~~ !!     .:XUW$W!~ "~:    :
              #"~~.:x%!!  !H:   !WM$$$$Ti.: .!WUn+!
              :::~:!!:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
              .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! 
              Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
              $R@i.~~ !     :   ~$$$$$B$$en:
              ?MXT@Wx.~    :     ~"##*$$$$M~
    """

    static_menu_text = """
                           ┓┏┓          ┏┳┓    ┓
                           ┃┫ ┏┓┏┓┏┳┓┏┓  ┃ ┏┓┏┓┃
                           ┛┗┛┗┻┛ ┛┗┗┗┻  ┻ ┗┛┗┛┗
                      
                                   Dev : 99k
                                  Version 1.0
[Menu]


[1] - Choisir un thème
[3] - Quitter
    """
    ascii_lines = ascii_art_text.splitlines()
    
    steps = len(ascii_lines)
    shift = 0
    
    while True:
        clear_screen()
        print("\033[H", end="")
        
        gradient = get_color_gradient(theme_rgb, (0, 0, 0), steps)
        
        for i, line in enumerate(ascii_lines):
            if line.strip():
                print(gradient[i] + line + '\033[0m')
        
        print(f'\033[38;2;{theme_rgb[0]};{theme_rgb[1]};{theme_rgb[2]}m' + static_menu_text + '\033[0m')
        
        shift += 1
        
        choix = input(f'\033[38;2;{theme_rgb[0]};{theme_rgb[1]};{theme_rgb[2]}m' + "┌──(user@karma)-[~/Menu]\n│\n└─$ " + '\033[0m')
        
        if choix == '1':
            clear_screen()
            theme_color_name, theme_rgb = choose_theme(theme_rgb)
            if theme_color_name == 'BACK':
                continue
        elif choix == '3':
            clear_screen()
            print(f'\033[38;2;{theme_rgb[0]};{theme_rgb[1]};{theme_rgb[2]}m' + "Vous avez choisi de quitter. Au revoir!" + '\033[0m')
            break
        else:
            clear_screen()
            print(f'\033[38;2;{theme_rgb[0]};{theme_rgb[1]};{theme_rgb[2]}m' + "Option invalide, veuillez réessayer." + '\033[0m')
            time.sleep(2)

def choose_theme(current_rgb):
    ascii_theme_art = r"""          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '"""

    ascii_theme_footer = """
                           ┓┏┓          ┏┳┓    ┓
                           ┃┫ ┏┓┏┓┏┳┓┏┓  ┃ ┏┓┏┓┃
                           ┛┗┛┗┻┛ ┛┗┗┗┻  ┻ ┗┛┗┛┗
                      
                                   Dev : 99k
                                  Version 1.0
                            
[Theme]
                               """

    # Splitting the ASCII art for gradient
    ascii_theme_art_lines = ascii_theme_art.splitlines()
    steps = len(ascii_theme_art_lines)
    
    # Applying gradient only to the ASCII art part
    gradient = get_color_gradient(current_rgb, (0, 0, 0), steps)
    
    for i, line in enumerate(ascii_theme_art_lines):
        if line.strip():
            print(gradient[i] + line + '\033[0m')
    
    # Printing the non-gradient footer
    print(f'\033[38;2;{current_rgb[0]};{current_rgb[1]};{current_rgb[2]}m' + ascii_theme_footer)

    print('\033[38;2;255;0;0m' + "[1] - RED" + '\033[0m' + "     \033[38;2;255;0;0m███████\033[0m")
    print('\033[38;2;50;205;50m' + "[2] - LIME" + '\033[0m' + "    \033[38;2;50;205;50m███████\033[0m")
    print('\033[38;2;0;0;255m' + "[3] - BLUE" + '\033[0m' + "    \033[38;2;0;0;255m███████\033[0m")
    print('\033[38;2;128;0;128m' + "[4] - PURPLE" + '\033[0m' + "  \033[38;2;128;0;128m███████\033[0m")
    print('\033[38;2;255;192;203m' + "[5] - PINK" + '\033[0m' + "    \033[38;2;255;192;203m███████\033[0m")
    print('\033[38;2;255;165;0m' + "[6] - ORANGE" + '\033[0m' + "  \033[38;2;255;165;0m███████\033[0m")
    print(f'\033[38;2;{current_rgb[0]};{current_rgb[1]};{current_rgb[2]}m' + "[b] - Retour au menu principal" + '\033[0m')

    choix = input(f'\033[38;2;{current_rgb[0]};{current_rgb[1]};{current_rgb[2]}m' + "┌──(user@karma)-[~/Menu/Thème]\n│\n└─$ " + '\033[0m')
    
    if choix == '1':
        return 'RED', (255, 0, 0)
    elif choix == '2':
        return 'LIME', (50, 205, 50)
    elif choix == '3':
        return 'BLUE', (0, 0, 255)
    elif choix == '4':
        return 'PURPLE', (138, 43, 226)
    elif choix == '5':
        return 'PINK', (255, 105, 180)
    elif choix == '6':
        return 'ORANGE', (255, 165, 0)
    elif choix.lower() == 'b':
        return 'BACK', current_rgb
    else:
        print('\033[38;2;255;0;0m' + "Choix invalide, thème par défaut (Rouge) sélectionné." + '\033[0m')
        return 'RED', (255, 0, 0)


if __name__ == "__main__":
    main_menu()
