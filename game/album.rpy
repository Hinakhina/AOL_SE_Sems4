init python:
    gallery = Gallery()

    gallery.button("play")
    gallery.unlock_image("CG_playing_card")
    gallery.condition("CG_playing_unlocked")

    gallery.button("spend")
    gallery.unlock_image("CG_spending_time")
    gallery.condition("CG_spending_unlocked")

    gallery.button("night")
    gallery.unlock_image("CG_park_night")
    gallery.condition("CG_night_unlocked")

    gallery.button("desk")
    gallery.unlock_image("CG_leaning_desk")
    gallery.condition("CG_desk_unlocked")

    gallery.button("good")
    gallery.unlock_image("CG_good_ending")
    gallery.condition("CG_good_unlocked")

    gallery.button("bad")
    gallery.unlock_image("CG_bad_ending")
    gallery.condition("CG_bad_unlocked")

screen album:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        grid 3 3:
            add gallery.make_button(name="play", unlocked="images/CGs/playing_card.jpg", locked="gui/ending.png")
            add gallery.make_button(name="spend", unlocked="images/CGs/spending_time.jpg", locked="gui/ending.png")
            add gallery.make_button(name="nigt", unlocked="images/CGs/park_night.jpg", locked="gui/ending.png")
            add gallery.make_button(name="desk", unlocked="images/CGs/leaning_desk.jpg", locked="gui/ending.png")
            add gallery.make_button(name="good", unlocked="images/CGs/good_ending.jpg", locked="gui/ending.png")
            add gallery.make_button(name="bad", unlocked="images/CGs/bad_ending.jpg", locked="gui/ending.png")
            textbutton "Return" action Return()