init python:
    gallery = Gallery()

    # Buttons for Love Interest A
    gallery.button("play")
    gallery.unlock_image("CG_playing_card")
    # gallery.condition("CG_playing_unlocked")

    gallery.button("spend")
    gallery.unlock_image("CG_spending_time")
    # gallery.condition("CG_spending_unlocked")

    gallery.button("night")
    gallery.unlock_image("CG_park_night")
    # gallery.condition("CG_night_unlocked")

    gallery.button("desk")
    gallery.unlock_image("CG_leaning_desk")
    # gallery.condition("CG_desk_unlocked")


    # Buttons for Love Interest B
    gallery.button("good")
    gallery.unlock_image("CG_good_ending")
    # gallery.condition("CG_good_unlocked")

    gallery.button("bad")
    gallery.unlock_image("CG_bad_ending")
    # gallery.condition("CG_bad_unlocked")


    # Buttons for Love Interest C
    # gallery.button("letter1")
    # gallery.unlock_image("CG_letter1")
    # gallery.condition("CG_letter1_unlocked")

    # gallery.button("letter2")
    # gallery.unlock_image("CG_letter2")
    # gallery.condition("CG_letter2_unlocked")
    
    # gallery.button("letter3")
    # gallery.unlock_image("CG_letter3")
    # gallery.condition("CG_letter3_unlocked")

    # gallery.button("hidden")
    # gallery.unlock_image("CG_hidden_letter")
    # gallery.condition("CG_hidden_unlocked")
    
    gallery.transition = dissolve