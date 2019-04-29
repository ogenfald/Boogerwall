define b = Character("Brandon")
define w = Character("Wall-chan")

label start:

    play music "/sound/game.mp3"

    scene bg house

    with fade

    "Brandon has just bought a new home and is beyond excited"

    show brandon daper
    with dissolve

    b "Ahhh, my new home. I can't wait to start my new life here"

    scene bg dining
    with fade

    pause 1

    scene bg living

    with fade

    pause 1

    scene bg kitchen

    with fade

    pause 1

    scene bg living
    
    with fade

    show brandon sad
    with dissolve

    b "Hmmm, its not quite what I expected. But I think it will work."
    
    w "...Konichiwa Brandon-san..."
    
    show brandon happy
    
    b "Who's there ?!"

    hide brandon happy
    
    show wall embarrassed
    with dissolve
    
    w "...I'm Wall-chan. I make up this space. I hope you like being inside of me."
    
    show brandon sad at left
    with dissolve
    
    show wall at right
    with dissolve
    
    "..."
    
    show wall nervous at right
    
    w "...Did I do something wrong?"
    
    b "No. I am just a man with very specific desires..."
    
    show wall at right
    
    w "I want you to enjoy being inside of me. I'm willing to do anything for you Brandon-san. Tell me your desires!"
    
    b "No, they are far too kinky for general conversation."
    
    show wall nervous at right
    
    "..."
    
    "...."
    
    show wall at right
    
    w "I am ready. Please share your deepest fantasies with me."
    
    show brandon happy at left
    
    b "Fine. I have alway been particulary interested in covering someone like yourself with..."
    
    show wall nervous at right
    
    w "With what Brandon-san?!"
    
    "..."
    
    b "With boogers"
    
    show wall embarrassed at right
    
    w " I see..."
    
    menu:
        "Allow Brandon to cover me with boogers":
            jump good
            
        "Tell him you are uncomfortable with such an act":
            jump bad
            
    label good:
        w "I will let you perform these unspeakable acts upon me."
        
        b "Excellent. Please allow me to get more comfortable."
        
        w "As you wish Brandon-san"
        
        hide brandon happy
        
        pause 1
        
        show brandon surprised at left
        with vpunch
        
        b "My body is ready. Prepare to get covered!!!"
        
        show wall boogers
        with hpunch
        
        w "AAaaaaahhhHHHhhh kimochi ii!!!!!"
        
        b "Oh yes take them!"
        
        hide brandon surprised
        
        show brandon happy at left
        
        "*heavy breathing*"
        
        b "Thank you Wall-chan, you are amazing"
        
        scene bg house
        
        "You got the good ending"

        return
        
    label bad:
        w "No Brandon-san, I can not allow you to do this to me."
        
        show brandon sad at left
        
        b "I thought you said you would do anything for me."
        
        show wall at right
        
        w "I thought I could but I will not do that."
        
        w "You are a disgusting freak."
        
        hide wall
        with dissolve
        
        hide brandon sad
        with dissolve
        
        show brandon sad
        with dissolve
        
        "..."
        
        b "That didn't go the way I planned."
        
        show brandon happy
        
        b "I guess I can go make myself white pee in the bathroom."
        
        scene bg house
        
        "You got the bad ending."
        
        return

    return
