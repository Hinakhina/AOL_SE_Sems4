screen gallery_navigation:
    frame:
        xsize 300
        background None
        yalign 0.5
        xpos -319 
        vbox:
            style_prefix "gallery"

            text "Gallery":
                yoffset -270
                xoffset 10

            spacing 25
            # xalign 1.0
            textbutton "Sceneries": 
                action ShowMenu("gallery_sceneries") 
                yoffset -156
            textbutton "Endings": 
                action ShowMenu("gallery_endings") 
                yoffset -156
            textbutton "Letters": 
                action ShowMenu("gallery_letters")
                yoffset -156
            
            textbutton "Return":
                action ShowMenu("preferences")
                yoffset 246

style gallery_button_text:
    font gui.button_text_font
    size gui.button_text_size
    idle_color "#707070"
    hover_color gui.button_text_hover_color
    selected_color gui.button_text_selected_color
    insensitive_color gui.button_text_insensitive_color



style gallery_text:
    size gui.title_text_size
    color gui.accent_color
    font gui.interface_text_font