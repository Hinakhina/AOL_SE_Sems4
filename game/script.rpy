# The script of the game goes in this file.

image CG_playing_card = "images/CGs/playing_card.PNG"
image CG_spending_time = "images/CGs/spending_time.PNG"
image CG_park_night = "images/CGs/park_night.PNG"
image CG_leaning_desk = "images/CGs/leaning_desk.png"
image CG_good_ending = "images/CGs/good_ending.jpg"
image CG_bad_ending = "images/CGs/bad_ending.jpg"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define aright = Position(xalign=0.6)
define aleft = Position(xalign=0.3)

define voices = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']
# define voices = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    import random

    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Play one immediately
            renpy.sound.play(random.choice(voices), channel="sound")
            # Then queue N more
            for _ in range(30):  # Adjust this number as needed
                renpy.sound.queue(random.choice(voices), channel="sound", loop=False)

        elif event in ["slow_done", "end"]:
            renpy.sound.stop(channel="sound")

define haru = Character("Haru", callback = type_sound)
define natsu = Character("Natsu", callback = type_sound)
define psychologist = Character("Psychologist",callback = type_sound)
define mom = Character("Mom", callback = type_sound)

define nar_nvl = Character(None, kind=nvl, callback=type_sound, what_style="nvl_thought")
define credit_nvl = Character(None, kind=nvl, callback=type_sound, what_style="nvl_credit")
define adv_nvl = Character(None, kind=adv, callback=type_sound)

# The game starts here.
image splash = "presplash.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(3)

    scene black with dissolve
    with Pause(1)

    return

label start:
    scene bg loading
    with fade
    pause(1.0)

    scene bg black 
    with fade
    adv_nvl "You run away from grief until it finds you in the middle of a sunny street on a beautiful day."

    jump chapter1

label chapter1:
    scene bg park
    with fade

    # play music "audio/hospital_ambient.mp3" loop fadein 1.0
    show haru sad 
    with dissolve
    pause (2.0)
    show haru frown
    haru "Spring crept quietly this year, like a secret too shy to be spoken aloud."
    show haru sad
    pause(1.0)
    show haru frown
    haru "I was here again. Another mild fever. Another few days tucked behind white walls."
    show haru sad
    pause(1.0)
    # play sound "audio/cirp.mp3" noloop fadein 1.0

    show haru frown
    haru "They said it wasn\'t serious, but somehow it always felt heavier than that."
    show haru sad
    pause(1.0)
    show haru frown
    haru "Maybe because loneliness always adds its own weight."
    
    show haru sad at aleft
    with MoveTransition(0.5, enter_time_warp=_warper.easein)
    pause(1.0)

    # play sound "audio/steps.mp3" noloop fadein 1.0 
    
    show natsu hospital smile at aright
    with MoveTransition(1.0, enter=offscreenright, enter_time_warp=_warper.easein)
    stop sound

    pause(1.0)
    show natsu hospital talk 
    natsu "Hey. You look like you\'re about to cry. Are you okay?"
    show natsu hospital smile 

    menu:
        "{i}{b}(Smile awkwardly){/b}{/i}":
            jump choice_c1_1

        "{i}{b}(Look away shyly){/b}{/i}":
            jump choice_c1_2
        
        "Not really.":
            jump choice_c1_3


label choice_c1_1:
    show haru sad
    pause(1.0)
    show haru frown
    haru "I\'m fine. Just... the flowers are pretty, that\'s all."
    show haru sad
    pause(1.0)
    show natsu hospital smile 
    pause(1.0)
    show natsu hospital talk 
    natsu "They\'re alright, I guess. But they\'re not nearly as interesting as you."
    show natsu hospital smile 
    pause(1.0)
    jump continue_c1

label choice_c1_2:
    show haru sad
    pause(1.0)
    show haru frown
    haru "I didn\'t know how to respond. His voice felt like sunlight on a rainy day."
    show haru sad 
    pause(1.0)
    show natsu hospital smile 
    pause(1.0)
    show natsu hospital talk 
    natsu "Don\'t worry. I get it. Hospitals aren\'t exactly happy places."
    show natsu hospital smile 
    pause(1.0)
    jump continue_c1   

label choice_c1_3:
    show haru sad 
    pause(1.0)
    show haru frown
    haru "Not really. Being here again... it just sucks."
    show haru sad 
    pause(1.0)
    show natsu hospital smile 
    pause(1.0)
    show natsu hospital talk 
    natsu "Yeah. Been there. Actually... still here."
    show natsu hospital smile 
    pause(1.0)
    jump continue_c1   

label continue_c1:
    scene bg grey
    with fade

    pause(1.0)

    show haru smile
    with dissolve
    pause(1.0)
    show haru smile talk
    haru "That\'s how I met Natsu. A boy who lived more in hospital rooms than anywhere else. But he smiled like someone who had the whole world tucked into his pocket."
    show haru smile

    scene CG_playing_card
    with fade 
    adv_nvl "{b}(Days pass. Quick montage of Haru and Natsu playing cards, talking in the garden, laughing.){/b}"
    haru "We became best friends faster than spring melted into summer."
    haru "Every story he told was like a patch sewn into my chest — mending something I hadn't realized was torn."

    scene bg park
    with fade
    show natsu hospital smile at aright
    with dissolve
    pause(0.5)
    show natsu hospital talk 
    natsu "What would you miss the most about me?"
    show natsu hospital smile 
    pause(0.5)
    show haru frown at aleft
    pause(0.5)
    show haru frown at aleft
    haru "I\'ll miss borrowing your books to read your notes in the margins. The closest I came to reading your mind."
    show haru smile
    pause(1.0)

    scene bg hospital room night 
    with fade 
    show natsu hospital smile
    with dissolve
    pause(1.0)
    show natsu hospital talk
    natsu "But how can you love a person who is not whole?"
    show natsu hospital smile

    menu:
        "Who says you\'re not whole?":
            show natsu hospital smile at aleft
            with fade
            pause(0.5)
            show haru smile at aright
            with dissolve
            pause(0.5)
            show haru smile talk 
            haru "Who says you\'re not whole? Just because you\'re different doesn\'t mean you're incomplete."
            show haru smile
            pause(0.5)
            show natsu hospital talk
            natsu "You\'re strange, you know that?"
            show natsu hospital smile
            pause(1.0)
        "Because even broken things are beautiful.":
            show natsu hospital smile at aleft
            with fade
            pause(0.5)
            show haru smile at aright
            with dissolve
            pause(1.0)
            show haru smile talk 
            haru "Because you, like the moon, are not only beautiful when full. In all of your phases and fractions and ivory-white pieces, I love you."
            show haru smile 
            pause(0.5)
            show natsu hospital smile
            pause(1.0)
            show natsu hospital talk
            natsu  "You\'re really something else."
            show natsu hospital smile
            pause(1.0)
        "{i}{b}(Stay silent, but reach for his hand.){/b}{/i}":
            show natsu hospital smile at aleft
            with fade
            pause(0.5)
            show haru smile at center
            with MoveTransition(1.0, enter_time_warp=_warper.easein)
            haru "..."
            "{i}(Natsu looks surprised but squeezes Haru\'s hand tightly.){/i}"
            show natsu hospital smile
            pause(0.5)
            show natsu hospital talk
            natsu "{i}Thanks... Haru{/i}"
            show natsu hospital smile
            pause(0.5)
    
    scene CG_spending_time
    with fade
    adv_nvl "{b}(April){/b}"

    scene bg black 
    with fade
    # play sound "audio/emergency.mp4" loop 
    pause (2.0)
    adv_nvl "The walls of hospitals have heard more prayers than the walls of churches..."
    adv_nvl "Because love is felt most when it's leaving."
    # stop sound fadeout 1.0
    pause(2.0)

    scene bg hospital
    with fade
    show haru sad cry
    with dissolve
    pause(2.0)
    show haru frown cry
    haru "Lord, I worry that love is grief."
    show haru sad cry
    pause(1.0)
    show haru frown cry
    haru "Lord, I fear that this grief will last forever. I put on a brave face and pretend it doesn't bother me, but it does. It does. Where am I to store all this heartache?"
    show haru sad cry
    pause(1.0)

    adv_nvl "Nobody has ever measured, not even the poets, how much the heart can hold."

    scene bg hospital room night
    with fade
    show haru smile tear at aright
    with dissolve
    pause(2.0)
    show haru smile sad 
    haru "I came to the garden today. Alone."
    show haru smile tear
    pause(1.0)
    show haru smile sad 
    haru "The flowers were still blooming. But it felt like the whole world forgot how to be colorful."
    show haru smile tear 
    pause(2.0)

    jump epilog_chapter1

label epilog_chapter1:
    scene bg black
    with fade
    # play sound "audio/paper.mp4" noloop

    pause(1.0)
    show letter:
        xalign 0.5
        yalign 0.5
        xzoom 1.4
        yzoom 1.4
    with dissolve
    pause(2.0)
    nar_nvl ""

    nar_nvl "{i}{b}\n\n\nLetter from Natsu - 1 (unlocked){/b}{/i}"

    nar_nvl "\nDear Haru,"

    nar_nvl """    
        \n I never believed in miracles until you sat next to me.\n    
        You made my small world a little bigger, a little brighter.\n    
        Even if I'm not there anymore,\n    
        even if my name fades from the hospital logs and\n
        my room gets cleaned out —\n    
        know that you stitched something permanent into me.\n    
        Our friendship must always remain the one\n
        deathless thing in our lives.\n    
        Thank you for being my March flower.\n    
        My blue spring ride.    
    """
    
    nar_nvl "\n— Natsu"
    
    scene bg black
    with fade
    pause(2.0)

    nvl clear

    $ renpy.end_replay()

    jump chapter2


label chapter2:
    scene CG_park_night
    with fade
    # show natsu ghost smile at aleft:
    #     alpha 0.8
    # with dissolve
    adv_nvl "{i}(Soft blue-grey rain, petals clinging to the wet pavement. A ghost of a boy smiles faintly in the distance.){/i}"
    
    # hide natsu
    # with dissolve

    show haru sad at aright
    with dissolve
    show haru sad frown 
    haru "April came like a soft breath over the hills."
    show haru sad 
    show haru sad frown 
    haru "The rain bloomed every flower, every wound."
    show haru sad 
    show haru sad frown 
    haru "I was discharged from the hospital the day the cherry blossoms began to fall."
    show haru sad 
    show haru sad frown 
    haru "They told me to rest. To heal."
    show haru sad 
    show haru sad frown 
    haru "But how could I? When the moment I stepped outside—"
    show haru sad 
    show haru sad smile 
    show haru sad tear
    pause (2.0)
    show haru sad tear
    show haru sad smile 
    haru "There he was."
    show haru sad tear
    show haru sad smile 
    haru "Natsu."
    show haru sad tear

    # show natsu ghost smile at right:
    #     alpha 0.8
    # with dissolve
    show haru smile
    show haru smile talk 
    haru "Standing on the sidewalk, the hospital bracelet still around his wrist, smiling like he hadn't just died."
    show haru sad 
    show haru smile tear
    show haru smile sad
    haru "I should have screamed. I should have cried."
    show haru smile tear
    show haru smile sad
    haru "But instead, my heart said:\n\n\"There you are\""
    show haru smile tear
    show haru sad tear
    show haru sad cry

    scene bg bedroom rainy
    with fade
    # play music "audio/rain.mp4" loop
    show haru school sad at aright
    pause (1.0)
    show haru school sad frown 
    haru "I sat at my desk, trying to finish my homework."
    show haru school sad 
    pause (0.5)
    show haru school sad frown 
    haru "Outside, the rain painted the glass silver."
    show haru school sad 
    pause (0.5)
    show haru school sad frown 
    haru "Inside, he sat cross-legged on my bed, humming an off-key song, like it was the most natural thing in the world."
    show haru school sad
    pause (1.0)
    show haru school smile  at aright
    pause (1.0)

    show natsu ghost smile at aleft:
        alpha 0.8
    with dissolve
    pause (1.0)

    show haru school smile talk 
    haru "I can\'t touch him, but he is there. Even so, I don\'t mind it."
    show haru school smile
    menu:
        "{i}{b}(Reach out your hand quietly){/b}{/i}":
            show haru school smile at center
            with MoveTransition(1.0, enter_time_warp=_warper.easein)
            haru "..."
            pause(2.0)
            jump continue_c2
        "{i}{b}(Smile at him without a word){/b}{/i}":
            show haru smile talk
            haru "..."
            pause(2.0)
            jump continue_c2
        "{i}{b}(Whisper his name, just once){/b}{/i}":
            haru "Natsu..."
            pause(2.0)
            jump continue_c2

label continue_c2:
    scene bg park
    with fade
    adv_nvl "{i}Day by day passed{/i}"

    scene bg bedroom rainy
    with fade
    pause (2.0)

    show haru smile at aright
    with dissolve
    pause (0.5)
    show natsu ghost smile at aleft
    with dissolve
    pause (0.5)
    show haru smile talk
    haru "\"Natsu, Natsu!\""
    show haru smile
    pause(2.0)
    hide natsu
    with dissolve
    pause (0.5)
    hide haru with dissolve
    show haru smile talk at aleft
    with dissolve
    haru "I say your name all the time when you're not around, just to put more of you in the world."
    show haru smile
    pause (0.5)

    show natsu ghost smile at aright:
        alpha 0.8
    with dissolve
    pause (1.0)

    show natsu ghost talk 
    natsu "You care for me, I feel it like an ax in my chest."
    show natsu ghost smile 
    pause (0.5)
    show natsu ghost talk 
    natsu "I didn't mean to stay like this…"
    show natsu ghost smile 
    pause (1.0)

    hide natsu
    with dissolve
    hide haru with fade
    pause (0.5)

    show haru sad at center
    with dissolve
    pause (1.0)

    show haru frown
    haru "My first feeling about the rain was that it was like you."
    show haru sad
    pause (0.5)
    show haru frown
    haru "Gentle. Endless. Impossible to hold."
    show haru sad
    pause (0.5)
    haru "..."
    pause (0.5)
    show haru frown
    haru "I miss you more than words can express."
    show haru sad
    pause (0.5)

    scene bg park 
    with fade 
    show haru sad at aleft
    pause (0.5)
    show haru frown 
    haru "Some days, I would see him in the crowd at school."
    show haru sad 
    pause (0.5)
    show haru frown 
    haru "Some nights, he would curl up by my window like a stray cat."
    show haru sad 
    pause (0.5)
    show haru frown 
    haru "No one else saw him."
    show haru sad
    pause (0.5) 
    show haru frown 
    haru "Maybe he wasn\'t real."
    show haru sad 
    pause (0.5)
    show haru frown 
    haru "Maybe I didn\'t care."
    show haru sad
    pause (0.5) 
    show haru frown 
    haru "Because he smiled. And talked. And stayed."
    show haru smile sad
    pause (1.5)


    jump epilog_chapter2


label epilog_chapter2:
    scene bg black
    with fade


    adv_nvl "{b}{i}April showers wash away the footprints, but not the memory.{/i}{/b}"
    

    pause(1.0)

    scene bg black with fade 
    nvl clear
    # play sound "audio/paper.mp4" noloop

    show letter:
        xalign 0.5
        yalign 0.5
        xzoom 1.4
        yzoom 1.4
    with dissolve
    pause(2.0)

    nar_nvl ""

    nar_nvl "{i}{b}\n\n\nLetter from Natsu - 2 (unlocked){/b}{/i}\n\n"

    nar_nvl """
        Haru,\n\n 
        I want you to know,\n 
        if you ever read this,\n 
        there was a time when I would rather have had you\n
        by my side than any one of these worlds;\n 
        I would rather have had you\n 
        by my side than all the books in the world.\n
    """

    scene black
    with dissolve
    pause(0.2)

    nvl clear

    $ renpy.end_replay()

    jump epilog_chapter2_2

    

label epilog_chapter2_2:
    
    scene bg black
    with fade

    # play sound "audio/paper.mp4" noloop

    pause(1.0)
    show letter:
        xalign 0.5
        yalign 0.5
        xzoom 1.4
        yzoom 1.4
    with dissolve
    pause(2.0)

    nar_nvl " "

    nar_nvl "{i}{b}\n\n\nLetter from Natsu - 3 (unlocked){/b}{/i}\n\n"

    nar_nvl """
    Haru,\n\n 
    since meeting you,\n 
    I actually began wishing for more time.\n 
    I want more time with you.\n
    """

    scene black
    with fade
    pause(2.0)

    nvl clear

    $ renpy.end_replay()

    jump chapter3_part1


label chapter3_part1:
    scene bg black 
    with fade
    adv_nvl "{b}(Present Day){/b}"

    scene bg park
    with fade

    show haru sad at aright
    with dissolve
    pause(0.5)
    show haru frown 
    haru "First day of June and I miss you more than ever."
    show haru sad 
    pause(0.5)
    hide haru
    adv_nvl "The summer sun felt suffocating, as if it could never truly reach Haru anymore."
    adv_nvl "Everything around her was alive with color, birds chirping, trees swaying, but inside her, it felt like everything had stopped."

    show haru sad 
    pause(0.5)
    show haru frown 
    haru "Your name, Natsu, it means Summer, but where were you? I can't seem to find you. It's summer already."
    show haru sad
    pause(0.5)

    hide haru with dissolve
    adv_nvl "The thought echoed constantly in her mind. He was gone—truly gone."

    show haru sad at aright
    with dissolve
    pause(0.5)
    show haru frown at aright
    haru "You said you are a ghost now? Haunt me, then!"
    show haru sad at aright
    pause(0.5)
    show haru frown at aright
    haru "Show up in the wind, be with me always. Only do not leave me in this abyss, where I cannot find you."
    show haru sad at aright
    pause(0.5)

    hide haru with fade
    pause(0.5)
    adv_nvl "She walked through the days mechanically. The laughter of her friends seemed distant, a world apart from the one she now inhabited." 
    adv_nvl "Grief was a constant companion, settling into her bones like a weight she could never escape."

    adv_nvl "But the worst part? She didn\'t even know how to ask for help. How do you explain the hole someone left behind? How do you say you\'re slowly drowning in silence when no one seems to notice?"

    adv_nvl "The world kept turning, but Haru couldn\'t keep up."


    show haru sad at aright
    with dissolve
    pause(0.5)
    show haru frown 
    haru "When I am asked how did I develop depression, I talk about the indifference of nature. It was soon after Natsu died, a brilliant April day, everything blooming."
    show haru sad 
    pause(0.5)

    hide haru with fade
    pause(0.5)
    adv_nvl "The days felt like they were on repeat. The same sun, the same sky, the same ache. And yet, it was as if nothing had changed. Not really. Not for her."

    show haru sad cry at aright
    with dissolve
    pause(0.5)
    show haru frown cry 
    haru "If l were fire, I would burn; If l were a woodcutter, I would strike. But I am a heart, and I love, and I grief. Would you come back to me?"
    show haru sad cry 
    pause(0.5)

    # play sound "audio/wind.mp4" noloop

    show haru frown cry 
    haru "When the rush of that wind came, Natsu, it was almost you."
    show haru sad cry 
    pause(0.5)

    scene bg kitchen
    with fade

    show haru sad with dissolve
    menu:
        "Mom, Dad... I have something to say.":
            show haru sad
            adv_nvl "{i}Her voice shook as she spoke, something she had never let anyone hear before.{/i}"
            show haru frown
            haru "I... I don\'t feel right. I can\'t stop thinking about Natsu. Everything feels so distant. I don\'t know how to live like this anymore."
            show haru sad
            hide haru with dissolve
            pause(0.5)
            show mom silent with dissolve
            pause(0.5)
            show mom talk
            mom "Thanks for telling us, dear. You don\'t have to go through this alone. Maybe it\'s time to talk to someone who can really help."
            show mom silent
            pause(1.0)
            jump chapter3_part2

        "Mom, Dad... Nevermind.":
            show haru sad
            adv_nvl "{i}The words stayed lodged in her throat, too heavy to lift. She smiled and nodded as her parents spoke, but inside, her heart cracked. She wasn\'t ready to tell them. Maybe they wouldn\'t understand. Or maybe it wouldn\'t matter.{/i}"
            show haru frown
            haru "How do we tell the sea that we are drowning on land?" 
            show haru sad
            pause(0.5)
            show haru frown
            haru "My grief barely literate."
            show haru sad tear
            pause(1.0)
            show haru sad cry
            pause(2.0)
            jump chapter3_part2

label chapter3_part2:
    scene bg bedroom rainy
    with fade
    adv_nvl "The silence in her room was deafening. She stared at the walls, the photos on her desk, all the things Natsu had touched." 
    adv_nvl "It was as if her life had stopped moving. The ache inside her chest was relentless, never letting go."
    
    show haru sad at center 
    with dissolve
    pause(0.5)
    show haru sad tear
    pause(1.0)
    show haru sad cry
    pause(1.0)
    show haru frown cry
    haru "We spoke endlessly about everything and nothing. Now, I cannot even remember the sound of your voice."
    hide haru with fade
    pause(1.0)

    adv_nvl "{b}Days blurred into weeks, but the world outside her window still turned.{/b}" 
    adv_nvl "{b}Flowers bloomed, birds sang, and people lived their lives—everyone except Haru, who was stuck in a place where the pain never seemed to lessen.{/b}"

    show haru sad cry
    pause(0.5)
    show haru frown cry
    haru "Natsu, Natsu! The past couple of days I\'ve missed you so much it felt like missing you is all I am. If my grief is violent enough, perhaps will you come back to life again?"
    show haru sad cry
    pause(0.5)
    show haru frown cry
    haru "I still wake up with things to tell you."
    show haru sad cry
    pause(1.0)

    scene CG_leaning_desk
    with fade
    pause(2.0)

    # play sound "" noloop

    scene bg grey
    with fade
    pause(1.0)

    adv_nvl "{i}She found herself reaching for the phone again, the number her mother had given her so many weeks ago still fresh in her mind.{/i}" 
    adv_nvl "{i}{b}\"It\'s okay to ask for help,\"{/b} she thought. But fear held her back.{/i}"

    menu:
        "I should face this grief head-on {i}{b}(call a psychologist){/b}{/i}":
            jump option1_c3_p2

        "I can manage this alone {i}{b}(avoid the call){/b}{/i}":
            jump option2_c3_p2
            

    return 


label option1_c3_p2:
    scene black with fade
    adv_nvl "{b}The phone rang once, then twice. Each ring felt like an eternity.{/b}" 
    adv_nvl "{b}But when the voice on the other end answered, Haru\'s heart skipped a beat. The calmness in the voice soothed her, a warmth she hadn\'t realized she was missing.{/b}"

    show haru sad tear at center 
    with dissolve
    pause(0.5)
    show haru frown sad
    haru "I... I'm not okay,"
    show haru sad tear
    pause(0.5)
    show haru frown sad
    haru "It\'s about my best friend. I don\'t know how to move on from his death. I\'m lost."
    show haru sad tear
    pause(0.5)

    scene bg grey gradien
    with fade

    show psychologist smile with dissolve
    pause(0.5)
    show psychologist talk
    psychologist "It\'s okay, take your time. You can tell me all of your concerns. There\'s only so long you can hold out against a force so strong the whole room can feel it."
    show psychologist smile
    pause(1.0)

    hide psychologist with fade 
    adv_nvl "{b}The psychologist, gentle and understanding, listened carefully, guiding her to speak.{/b}" 
    adv_nvl "{b}It felt strange, at first, to voice her pain to a stranger, but slowly, she began to unravel. And with each word she said, the weight on her chest became a little lighter.{/b}"

    scene black 
    with dissolve
    pause(1.0)

    jump chapter3_part3

label option2_c3_p2:
    adv_nvl "{b}She stared at the phone, her fingers frozen over the screen. She wanted to call. She knew she needed to call. But the thought of exposing her vulnerabilities, her deepest pain, kept her paralyzed.{/b}"

    show haru sad at center
    with dissolve
    pause(0.5)
    show haru frown
    haru "I am not well. I could have built the Pyramids with the effort it takes me to cling on to life."
    show haru sad
    pause(0.5)
    show haru frown
    haru "I ache and swell in a hundred places, but mostly in the middle of my heart. I want to die. Leave me alone. I feel I am almost there- where the great terror can dismember me."
    show haru sad
    pause(0.5)
    
    scene black 
    with fade

    adv_nvl "{b}Haru turned away, as she had done countless times before. Maybe another time. Maybe tomorrow. But deep down, she knew she couldn\'t keep running from the grief forever.{/b}"
    pause(1.0)
    jump chapter3_part3

label chapter3_part3:
    scene bg park
    with fade 

    adv_nvl "{b}The days bled into one another, but something shifted within Haru. Slowly, she began to feel the stirrings of something.{/b}"
    show haru sad with dissolve
    menu:
        "{i}{b}(Embraces the journey of healing, learning to live with the grief.){/b}{/i}":
            scene bg hospital 
            with fade
            show haru smile at aleft
            with dissolve
            show psychologist smile at aright
            adv_nvl "Haru attended her therapy sessions regularly, and each time, she found herself a little more whole." 
            hide psychologist
            with fade

            show haru smile at center
            adv_nvl "She began journaling, capturing her thoughts and feelings in ways she never thought possible. It didn\'t feel like a cure, but more like a step forward."

            adv_nvl "The world began to regain its colors again. Natsu\'s memory, while still painful, became a source of love rather than just sorrow."
            
            adv_nvl "She even smiled sometimes—without guilt, without fear. It was okay to be happy again."
            show haru smile tear
            pause(0.5)
            show haru smile sad
            haru "To lose someone you love is to alter your life for ever. You don\'t get over it because \'it\' is the person you loved. The pain stops, there are new people, but the gap never closes. How could it? The particularness of.someone who mattered enough to grieve over is not made anodyne by death. This hole in my heart is in the shape of you and no-one else can fit it. Why would I want them to?"
            show haru smile tear
            pause(0.5)
            show haru smile sad
            haru "After Natsu died, the world became very clear-as if a window had broken--the world itself became very dear. It was the place Natsu had lived, and as long as I still walked around I could catch glimpses of him. But more than that, when Natsu died I felt as if l had finally entered the larger community of humans"
            show haru smile tear
            pause(0.5)
            show haru smile sad cry talk
            haru "Now I knew unbearable grief, and I was like other people in this world who had known this. I began to understand that everything I knew and loved would pass away, and I would pass away. I would die like my best friend had died, and the world, the actual \"is-ness\" of it became and remains very precious to me, the wind, running water, voices"
            show haru sad cry
            pause(1.0)
            jump good_ending_c3_p4
        
        "{i}{b}(Try to forget about the grief entirely, pushing it down again.){/b}{/i}":
            scene black with fade
            adv_nvl "The days continued to pass, and Haru tried to go through life as if nothing had changed. She buried the grief deeper, not allowing herself the space to mourn. She convinced herself it was easier this way, that if she just ignored it, the pain would go away…"

            show haru sad with dissolve
            pause(0.5)
            show haru frown 
            haru "They say, if you immerse your feet in icy water you forget grief for a moment. I did this once, my brother made us cross a cold stream barefoot, that summer, walking in the woods-l was emptied, then elated, blissful; but didn't try it again. Grief returns vengeful after you've repulsed it"

            hide haru with fade
            pause(0.5)
            adv_nvl "...but it never did. Her grief came back tenfold, a shadow she could never escape."
            adv_nvl "It lived in the corners of her laughter, in the weight of her silences, and in the moments she dared to remember."

            show haru sad cry with dissolve
            pause(0.5)
            show haru frown cry with dissolve
            haru "I found him in grief. Which was ever present."
            show haru sad cry with dissolve
            pause(0.5)
            show haru frown cry with dissolve
            haru "Time has flown, and I have not flown with it. I exist, that is all, and I find it nauseating."
            show haru sad cry with dissolve
            pause(1.0)
            jump bad_ending_c3_part4

label good_ending_c3_p4:
    scene bg hospital with fade
    show haru smile with dissolve
    adv_nvl "{b}By seeking help and confronting her grief, Haru was able to reclaim parts of herself that she had lost. Through therapy, she learned that while grief would never fully disappear, she could heal and live on.{/b}"

    hide haru with dissolve
    pause(0.5)
    show CG_good_ending with fade
    pause(2.0)
    adv_nvl "{b}Her relationship with Natsu\'s memory remained, but it was no longer a source of overwhelming pain.{/b}"
    adv_nvl "{b}Sometimes grief is acceptance that love has always been inadequate. Sometimes it\'s just another day and the light comes in through the window.{/b}"
    
    haru "When I turned to face grief, I saw that it was just love in a heavy coat."
    haru "I know I'll always think of Natsu with something like hurt and nostalgia - and a great deal of love."
    adv_nvl "{b}- THE END -\n- Good Ending -{/b}"
    pause(3.0)

    scene black with dissolve
    jump hidden_note

label bad_ending_c3_part4:
    scene CG_bad_ending with fade
    pause(2.0)
    adv_nvl "{b}Haru, having avoided the help she needed, continued to live under the weight of her grief.{/b}"
    adv_nvl "{b}While the world continued to move on around her, Haru remained in stasis—unwilling to face the truth of her pain. Her grief, unaddressed, would continue to haunt her.{/b}"

    haru "I hurled myself into my grief like a dove, like snow on the dead. Angels don't know whether they're moving among the living or the dead."

    adv_nvl "{b}- The END -\n-Bad Ending -{/b}"
    pause(3.0)

    scene black with dissolve

    jump hidden_note

label hidden_note:
    scene bg white with fade
    # play sound "audio/letter.mp4" noloop
    adv_nvl "{b}Hidden Note - (Unlocked){/b}\n"

    # play sound "audio/paper.mp4" noloop
    scene bg black with fade
    show letter:
        xalign 0.5
        yalign 0.5
        xzoom 1.4
        yzoom 1.4
    with dissolve
    pause(2.0)

    nar_nvl ""

    nar_nvl"""
    \n\nAuthor\'s Note:\n\n 
    I sat on a gray stone bench ringed with \n 
    the ingénue faces of pink and white impatiens\n 
    and placed my grief in the mouth of language,\n 
    the only thing that would grieve with me.\n\n 
    My writing was about you.\n 
    All I was bewailing in it was\n 
    what I could not weep about on your shoulder.\n 
    I want to write rage but all\n 
    that comes is sadness.\n\n 
    Acceptance.\n 
    I finally reach it.\n 
    But something is wrong.\n 
    Grief is a circular staircase,\n 
    I have lost you.\n

    """
    pause(2.0)
    scene bg black with fade

    nvl clear

    $ renpy.end_replay()
    
    jump end_credit


label end_credit:
    scene bg black with fade

    credit_nvl """
    🌸 End Credits Message – \"To Those Who Are Still Here\" 🌸\n 
    \"You hold an absence at your center, as if it were a life.\"\n 
    This story was born from grief, but it does not end there.\n 
    If you saw yourself in Haru, please know:\n 
    You are not alone. Your pain is real. And help is out there.\n 
    Mental health matters. Just as much as physical health.\n 
    Just as much as your life.\n\n 
    🕊️ If you\'re struggling, we encourage you to reach out:\n 
    Indonesia:\n 
    Pijar Psikologi — {a=https://pijarpsikologi.org}https://pijarpsikologi.org{/a}\n 
    Into The Light Indonesia — {a=https://intothelightid.org}https://intothelightid.org{/a}\n 
    Kemenkes Hotline 119 ext. 8\n\n 
    International:\n 
    Mental Health Hotlines (Befrienders Worldwide) — {a=https://www.befrienders.org}https://www.befrienders.org{/a}\n 
    Lifeline (US) — 988 or {a=https://988lifeline.org}https://988lifeline.org{/a}\n 
    Samaritans (UK) — 116 123\n\n 
    💬 Talk to someone. A friend. A family member. A counselor. A helpline.\n 
    Opening up is not weakness. It\'s courage.\n 
    Thank you for playing.\n 
    Thank you for staying.\n\n  
    — The Dev Team\n  
    🎗️ SDG 3: Good Health & Well-Being\n 
    Because everyone deserves access to healing—body and mind.\n 
    """
    return  

    
