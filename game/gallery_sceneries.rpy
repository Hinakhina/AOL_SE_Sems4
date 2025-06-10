screen gallery_sceneries:
    tag menu
    add "gui/overlay/game_menu.png"
    hbox:
        # xpos gui.navigation_xpos
        # spacing 100
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation
        
        
        grid 2 2:
            spacing 25 
            
            add gallery.make_button(name="play", unlocked=im.Scale("images/CGs/playing_card.PNG", 425, 228), locked="gui/ending.png")
            add gallery.make_button(name="spend", unlocked=im.Scale("images/CGs/spending_time.PNG", 425, 228), locked="gui/ending.png")
            add gallery.make_button(name="night", unlocked=im.Scale("images/CGs/park_night.PNG", 425, 228), locked="gui/ending.png")
            add gallery.make_button(name="desk", unlocked=im.Scale("images/CGs/leaning_desk.png", 425, 228), locked="gui/ending.png")
           