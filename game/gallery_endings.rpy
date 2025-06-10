screen gallery_endings:
    tag menu
    add "gui/overlay/game_menu.png"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation

        grid 2 1:
            spacing 25

            add gallery.make_button(name="good", unlocked=im.Scale("images/CGs/good_ending.jpg", 425, 228), locked="gui/ending.png")
            add gallery.make_button(name="bad", unlocked=im.Scale("images/CGs/bad_ending.jpg", 425, 228), locked="gui/ending.png")
           