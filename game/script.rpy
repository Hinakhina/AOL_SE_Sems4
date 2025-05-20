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
    "Letter from Natsu - 1 (unlocked)"

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

    jump chapter2

label chapter2:
    scene bg rain ghost
    show natsu ar right: alpha 0.5
    "(Soft blue-grey rain, petals clinging to the wet pavement. A ghost of a boy smiles faintly in the distance.)"
    
    hide natsu
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

    scene bg bedroom
    play music "audio/rain.mp4" loop
    show haru at right
    haru "I sat at my desk, trying to finish my homework."
    haru "Outside, the rain painted the glass silver."
    haru "Inside, he sat cross-legged on my bed, humming an off-key song, like it was the most natural thing in the world."

    show natsu at left: alpha 0.5
    haru "I can\'t touch him, but he is there. Even so, I don\'t mind it."

    menu:
        "[[Reach out your hand quietly]]":
            jump continue_c2
        "[[Smile at him without a word]]":
            jump continue_c2
        "[[Whisper his name, just once]]":
            jump continue_c2

label continue_c2:
    hide natsu
    haru "\"Natsu, Natsu!\""
    haru "I say your name all the time when you're not around, just to put more of you in the world."

    show natsu at left: alpha 0.5
    with dissolve
    natsu sorry "You care for me, I feel it like an ax in my chest."
    natsu sorry "I didn't mean to stay like this…"

    haru thinking "My first feeling about the rain was that it was like you."
    haru "Gentle. Endless. Impossible to hold."
    haru " "
    haru "I miss you more than words can express."

    scene bg school 
    with fade 
    show haru at left
    haru "Some days, I would see him in the crowd at school."
    haru "Some nights, he would curl up by my window like a stray cat."
    haru "No one else saw him."
    haru "Maybe he wasn’t real."
    haru "Maybe I didn’t care."
    haru "Because he smiled. And talked. And stayed."

    jump epilog_chapter2

label epilog_chapter2:
    scene black
    with fade

    "April showers wash away the footprints, but not the memory."
    
    play sound "audio/paper.mp4" noloop

    scene Letter
    with fade
    ""
    "Letter from Natsu - 2 (unlocked)"

    show add Solid(black)
    '''
    Haru, 

    I want you to know, 
    if you ever read this, 
    there was a time when I would rather have had you 
    by my side than any one of these worlds; 
    I would rather have had you 
    by my side than all the books in the world.
    '''

    show black
    with dissolve

    play sound "audio/paper.mp4" noloop

    scene Letter
    with fade
    ""
    "Letter from Natsu - 3 (unlocked)"

    show add Solid(black)
    '''
    Haru, 

    since meeting you, 
    I actually began wishing for more time. 
    I want more time with you.
    '''

    show black
    with dissolve

    jump chapter3_part1

label chapter3_part1:
    "(Present Day)"

    scene bg summer
    with fade

    show haru at right
    haru "First day of June and I miss you more than ever."

    hide haru
    "The summer sun felt suffocating, as if it could never truly reach Haru anymore."
    "Everything around her was alive with color, birds chirping, trees swaying, but inside her, it felt like everything had stopped."

    show haru at right
    haru thinking "Your name, Natsu, it means Summer, but where were you? I can't seem to find you. It's summer already."

    hide haru 
    "The thought echoed constantly in her mind. He was gone—truly gone."

    show haru at right
    haru thinking "You said you are a ghost now? Haunt me, then!"
    haru thinking "Show up in the wind, be with me always. Only do not leave me in this abyss, where I cannot find you."

    hide haru
    "She walked through the days mechanically. The laughter of her friends seemed distant, a world apart from the one she now inhabited." 
    "Grief was a constant companion, settling into her bones like a weight she could never escape."

    "But the worst part? She didn\'t even know how to ask for help."
    "How do you explain the hole someone left behind?"
    "How do you say you\'re slowly drowning in silence when no one seems to notice?"

    "The world kept turning, but Haru couldn\'t keep up."

    show haru at right
    haru "When I am asked how did I develop depression, I talk about the indifference of nature. It was soon after Natsu died, a brilliant April day, everything blooming."

    hide haru
    "The days felt like they were on repeat. The same sun, the same sky, the same ache. And yet, it was as if nothing had changed. Not really. Not for her."

    show haru at right
    haru crying "If l were fire, I would burn; If l were a woodcutter, I would strike. But I am a heart, and I love, and I grief. Would you come back to me?"

    play sound "audio/wind.mp4" noloop
    haru "When the rush of that wind came, Natsu, it was almost you."

    scene bg dining
    with fade
    show haru
    menu:
        "Mom, Dad... I have something to say.":
            "Her voice shook as she spoke, something she had never let anyone hear before."
            haru "I... I don\'t feel right. I can\'t stop thinking about Natsu. Everything feels so distant. I don't know how to live like this anymore."
            hide haru
            show mom concern
            mom "Thanks for telling us, dear. You don\'t have to go through this alone. Maybe it\'s time to talk to someone who can really help."
            jump chapter3_part2

        "Mom, Dad... Nevermind.":
            "The words stayed lodged in her throat, too heavy to lift. She smiled and nodded as her parents spoke, but inside, her heart cracked. She wasn’t ready to tell them. Maybe they wouldn't understand. Or maybe it wouldn’t matter."
            haru "How do we tell the sea that we are drowning on land?" 
            haru "My grief barely literate."
            jump chapter3_part2

label chapter3_part2:
    scene bg bedroom
    with fade
    "The silence in her room was deafening. She stared at the walls, the photos on her desk, all the things Natsu had touched." 
    "It was as if her life had stopped moving. The ache inside her chest was relentless, never letting go."
    
    show haru 
    haru "We spoke endlessly about everything and nothing. Now, I cannot even remember the sound of your voice."

    hide haru 
    "Days blurred into weeks, but the world outside her window still turned." 
    "Flowers bloomed, birds sang, and people lived their lives—everyone except Haru, who was stuck in a place where the pain never seemed to lessen."

    show haru 
    haru "Natsu, Natsu! The past couple of days I\'ve missed you so much it felt like missing you is all I am. If my grief is violent enough, perhaps will you come back to life again?"

    haru "I still wake up with things to tell you."

    show bg table
    with fade
    show bg telephone
    with fade

    "She found herself reaching for the phone again, the number her mother had given her so many weeks ago still fresh in her mind." 
    "\"It\'s okay to ask for help,\" she thought. But fear held her back."

    menu:
        "I should face this grief head-on [[call a psychologist]]":
            jump option1_c3_p2

        "I can manage this alone [[avoid the call]]":
            jump option2_c3_p2
            

    return 


label option1_c3_p2:
    scene black with fade
    "The phone rang once, then twice. Each ring felt like an eternity." 
    "But when the voice on the other end answered, Haru\'s heart skipped a beat. The calmness in the voice soothed her, a warmth she hadn\'t realized she was missing."

    show haru
    haru "I... I'm not okay,"
    haru "It’s about my best friend. I don\'t know how to move on from his death. I\'m lost."

    hide haru

    add Solid(white)

    show psychologist
    psychologist "It\'s okay, take your time. You can tell me all of your concerns. There\'s only so long you can hold out against a force so strong the whole room can feel it."

    hide psychologist
    "The psychologist, gentle and understanding, listened carefully, guiding her to speak." 
    "It felt strange, at first, to voice her pain to a stranger, but slowly, she began to unravel. And with each word she said, the weight on her chest became a little lighter."

    scene black with dissolve

    jump chapter3_part3

label option2_c3_p2:
    "She stared at the phone, her fingers frozen over the screen. She wanted to call. She knew she needed to call. But the thought of exposing her vulnerabilities, her deepest pain, kept her paralyzed."

    show haru 
    haru "I am not well. I could have built the Pyramids with the effort it takes me to cling on to life."
    haru "I ache and swell in a hundred places, but mostly in the middle of my heart. I want to die. Leave me alone. I feel I am almost there- where the great terror can dismember me."
    
    scene bg black with fade
    "Haru turned away, as she had done countless times before. Maybe another time. Maybe tomorrow. But deep down, she knew she couldn’t keep running from the grief forever."

    jump chapter3_part3

label chapter3_part3:
    scene bg park
    "The days bled into one another, but something shifted within Haru. Slowly, she began to feel the stirrings of something."
    show haru 
    menu:
        "[[Embraces the journey of healing, learning to live with the grief.]]":
            show bg hospital with fade
            show haru
            "Haru attended her therapy sessions regularly, and each time, she found herself a little more whole." 
            "She began journaling, capturing her thoughts and feelings in ways she never thought possible. It didn\'t feel like a cure, but more like a step forward."

            "The world began to regain its colors again. Natsu’s memory, while still painful, became a source of love rather than just sorrow."
            
            show haru happy
            
            "She even smiled sometimes—without guilt, without fear. It was okay to be happy again."
            haru "To lose someone you love is to alter your life for ever. You don't get over it because 'it' is the person you loved. The pain stops, there are new people, but the gap never closes. How could it? The particularness of.someone who mattered enough to grieve over is not made anodyne by death. This hole in my heart is in the shape of you and no-one else can fit it. Why would I want them to?"
            haru "After Natsu died, the world became very clear-as if a window had broken--the world itself became very dear. It was the place Natsu had lived, and as long as I still walked around I could catch glimpses of him. But more than that, when Natsu died I felt as if l had finally entered the larger community of humans"
            haru "Now I knew unbearable grief, and I was like other people in this world who had known this. I began to understand that everything I knew and loved would pass away, and I would pass away. I would die like my best friend had died, and the world, the actual \"is-ness\" of it became and remains very precious to me, the wind, running water, voices"
            jump to good_ending_c3_p4
        
        "[[Try to forget about the grief entirely, pushing it down again.]]":
            scene black with fade
            "The days continued to pass, and Haru tried to go through life as if nothing had changed. She buried the grief deeper, not allowing herself the space to mourn. She convinced herself it was easier this way, that if she just ignored it, the pain would go away…"

            show haru 
            haru "They say, if you immerse your feet in icy water you forget grief for a moment. I did this once, my brother made us cross a cold stream barefoot, that summer, walking in the woods-l was emptied, then elated, blissful; but didn't try it again. Grief returns vengeful after you've repulsed it"

            hide haru 
            "...but it never did. Her grief came back tenfold, a shadow she could never escape."
            "It lived in the corners of her laughter, in the weight of her silences, and in the moments she dared to remember."

            show haru 
            haru "I found him in grief. Which was ever present."
            haru "Time has flown, and I have not flown with it. I exist, that is all, and I find it nauseating."
            jump to bad_ending_c3_part4

label good_ending_c3_p4:
    scene bg hospital with fade
    show haru
    "By seeking help and confronting her grief, Haru was able to reclaim parts of herself that she had lost. Through therapy, she learned that while grief would never fully disappear, she could heal and live on."

    hide haru
    show bg good ending with dissolve
    "Her relationship with Natsu\'s memory remained, but it was no longer a source of overwhelming pain."
    "Sometimes grief is acceptance that love has always been inadequate. Sometimes it\'s just another day and the light comes in through the window."

    haru "When I turned to face grief, I saw that it was just love in a heavy coat."
    haru "I know I'll always think of Natsu with something like hurt and nostalgia - and a great deal of love."
    "- THE END -"
    "- Good Ending -"
    scene black with dissolve
    jump hidden_note

label bad_ending_c3_part4:
    scene bg bad ending with fade
    "Haru, having avoided the help she needed, continued to live under the weight of her grief."
    "While the world continued to move on around her, Haru remained in stasis—unwilling to face the truth of her pain. Her grief, unaddressed, would continue to haunt her."

    show haru
    haru "I hurled myself into my grief like a dove, like snow on the dead. Angels don't know whether they're moving among the living or the dead."

    "- The END -"
    "-Bad Ending -"

    scene black with dissolve

    jump hidden_note

label hidden_note:
    scene white with fade
    play sound "audio/letter.mp4" noloop
    "Author's Note (Unlocked)"

    show letter
    '''
    Author\'s Note:
    I sat on a gray stone bench ringed with 
    the ingénue faces of pink and white impatiens 
    and placed my grief in the mouth of language, 
    the only thing that would grieve with me.

    My writing was about you. 
    All I was bewailing in it was 
    what I could not weep about on your shoulder. 
    I want to write rage but all 
    that comes is sadness.

    Acceptance. 
    I finally reach it. 
    But something is wrong. 
    Grief is a circular staircase, 
    I have lost you.

    '''

    scene white with dissolve

    jump end_credit

label end_credit:
    scene black with fade
    '''
            🌸 End Credits Message – "To Those Who Are Still Here" 🌸
        “You hold an absence at your center, as if it were a life.”
        This story was born from grief—but it does not end there.
        If you saw yourself in Haru, please know:
        You are not alone. Your pain is real. And help is out there.
        Mental health matters. Just as much as physical health.
        Just as much as your life.
        
        🕊️ If you're struggling, we encourage you to reach out:
        Indonesia:
        Pijar Psikologi — https://pijarpsikologi.org
        Into The Light Indonesia — https://intothelightid.org
        Kemenkes Hotline 119 ext. 8


        International:
        Mental Health Hotlines (Befrienders Worldwide) — https://www.befrienders.org
        Lifeline (US) — 988 or https://988lifeline.org
        Samaritans (UK) — 116 123


        💬 Talk to someone. A friend. A family member. A counselor. A helpline.
        Opening up is not weakness. It\'s courage.
        
        Thank you for playing.
        Thank you for staying.
        
        — The Dev Team
        
        🎗️ SDG 3: Good Health & Well-Being
        Because everyone deserves access to healing—body and mind.
    '''
    return  

    
