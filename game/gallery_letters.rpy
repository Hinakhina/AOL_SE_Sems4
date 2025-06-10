screen gallery_letters:
    tag menu
    add "gui/overlay/game_menu.png"
    hbox:
        yalign 0.5
        xalign 0.5
        # xpos 0
        
        use gallery_navigation

        grid 2 2:
            spacing 25

            imagebutton: 
                idle im.Scale("images/CGs/letter1_idle.png", 425, 228) 
                hover im.Scale("images/CGs/letter1_hover.png", 425, 228)
                insensitive"gui/ending.png" 
                action Replay("epilog_chapter1")

            imagebutton: 
                idle im.Scale("images/CGs/letter2_idle.png", 425, 228) 
                hover im.Scale("images/CGs/letter2_hover.png", 425, 228) 
                insensitive"gui/ending.png" 
                action Replay("epilog_chapter2")

            imagebutton: 
                idle im.Scale("images/CGs/letter3_idle.png", 425, 228) 
                hover im.Scale("images/CGs/letter3_hover.png", 425, 228) 
                insensitive"gui/ending.png" 
                action Replay("epilog_chapter2_2")

            imagebutton: 
                idle im.Scale("images/CGs/hidden_letter_idle.png", 425, 228) 
                hover im.Scale("images/CGs/hidden_letter_hover.png", 425, 228) 
                insensitive"gui/ending.png" 
                action Replay("hidden_note")
            