# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define haru = Character("Haru", image="haru")
define pov = Character("[povname]")


# The game starts here.

label start:
    with fade
    scene bg loading
    with fade
    "You run away from grief until it finds you in the middle of a sunny street on a beautiful day."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show haru happy

    # These display lines of dialogue.

    haru "You\'ve created a new Ren\'Py game."

    haru "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label chapter1:
    scene bg hospital
    with fade
    play music "audio/hospital_ambient.mp3" loop fadein 1.0

    haru "Spring crept quietly this year, like a secret too shy to be spoken aloud."
    haru "I was here again. Another mild fever. Another few days tucked behind white walls."
    
    play sound "audio/cirp.mp3" noloop fadein 1.0

    haru "They said it wasn\'t serious, but somehow it always felt heavier than that."
    haru "Maybe because loneliness always adds its own weight."

    play sound "audio/steps.mp3" noloop fadein 1.0 

    natsu "Hey. You look like you\'re about to cry. Are you okay?"

    menu:
        "[[Smile awkwardly]]":
            jump choice_c1_1

        "[[Look away shyly]]":
            jump choice_c1_2
        
        "Not really.":
            jump choice_c1_3


label choice_c1_1:
    show haru at left
    show natsu at right
    haru "I\'m fine. Just... the flowers are pretty, that\'s all."
    natsu smirking "They\'re alright, I guess. But they\'re not nearly as interesting as you."
    jump continue_c1

label choice_c1_2:
    show haru at left
    show natsu at right
    haru thinking "I didn\'t know how to respond. His voice felt like sunlight on a rainy day."
    natsu gentle "Don\'t worry. I get it. Hospitals aren\'t exactly happy places."
    jump continue_c1   

label choice_c1_3:
    show haru at left
    show natsu at right
    haru "Not really. Being here again... it just sucks."
    natsu nodding "Yeah. Been there. Actually... still here."
    jump continue_c1   

label continue_c1:
    scene black
    with fade

    show haru
    haru "That\'s how I met Natsu. A boy who lived more in hospital rooms than anywhere else. But he smiled like someone who had the whole world tucked into his pocket."

    scene bg a
    with fade 
    "(Days pass. Quick montage of Haru and Natsu playing cards, talking in the garden, laughing.)"
    haru "We became best friends faster than spring melted into summer."
    haru "Every story he told was like a patch sewn into my chest — mending something I hadn't realized was torn."

    scene bg cherry tree
    with fade
    show natsu at left
    natsu "What would you miss the most about me?"

    show haru surprised at right
    haru quitely "I\'ll miss borrowing your books to read your notes in the margins. The closest I came to reading your mind."

    scene hospital night 
    with fade 
    natsu "But how can you love a person who is not whole?"

    menu:
        "Who says you\'re not whole?":
            haru "Who says you\'re not whole? Just because you\'re different doesn\'t mean you're incomplete."
            natsu smiling touched "You\'re strange, you know that?"
        "Because even broken things are beautiful.":
            haru "Because you, like the moon, are not only beautiful when full. In all of your phases and fractions and ivory-white pieces, I love you."
            natsu eyes wide "..."
            natsu laughing  "You\'re really something else."
        "[[Stay silent, but reach for his hand.]]"
            "(Natsu looks surprised but squeezes Haru\'s hand tightly.)"
            natsu whisper "Thanks... Haru"
    
    scene bg haru natsu
    with fade
    "(April)"

    scene black 
    with fade
    play sound "audio/emergency.mp4" loop 
    "The walls of hospitals have heard more prayers than the walls of churches..."
    "Because love is felt most when it's leaving."
    stop sound fadeout 1.0

    scene bg operating room
    with fade
    haru praying "Lord, I worry that love is grief."
    haru praying "Lord, I fear that this grief will last forever. I put on a brave face and pretend it doesn't bother me, but it does. It does. Where am I to store all this heartache?"

    "Nobody has ever measured, not even the poets, how much the heart can hold."

    scene bg rainy hospital bed
    with fade
    show haru at left
    haru "I came to the garden today. Alone."
    haru "The flowers were still blooming. But it felt like the whole world forgot how to be colorful."

    jump epilog_chapter1

label epilog_chapter1:
    scene black
    with fade
    play sound "audio/paper.mp4" noloop

    scene Letter
    with fade
    ""
    "Letter from Natsu (unlocked)"

    show add Solid(black)
    '''
    Dear Haru,

        I never believed in miracles until you sat next to me.
        You made my small world a little bigger, a little brighter.
        Even if I'm not there anymore, even if my name fades from the hospital logs and my room gets cleaned out —
        know that you stitched something permanent into me.
        Our friendship must always remain the one deathless thing in our lives.
        Thank you for being my March flower. My blue spring ride.
    
    — Natsu
    '''

    show black
    with dissolve

    return

label chapter2:
    scene bg rain ghost
    "(Soft blue-grey rain, petals clinging to the wet pavement. A ghost of a boy smiles faintly in the distance.)"
    
    show haru at left
    haru "April came like a soft breath over the hills."
    haru "The rain bloomed every flower, every wound."
    haru "I was discharged from the hospital the day the cherry blossoms began to fall."
    haru "They told me to rest. To heal."
    haru "But how could I? When the moment I stepped outside—"
    haru " "
    haru "There he was."
    haru "Natsu."
    show natsu at right: alpha 0.5
    haru "Standing on the sidewalk, the hospital bracelet still around his wrist, smiling like he hadn't just died."
    haru "I should have screamed. I should have cried."
    haru "But instead, my heart said:\n\n\"There you are\""


    
