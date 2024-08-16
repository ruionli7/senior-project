# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")
define nurse = Character("Nurse")
define unknown = Character("???")
define teacher = Character("Teacher")
define dad = Character("Dad")
define fish = Character("Prince Salaman")
define knife = Character("Cane")
define tree = Character ("Brunt")
define drooling = Character("Drooling Girl")
define girl = Character("Girl")
define girl1 = Character("Girl 1")
define girl2 = Character("Girl 2")
define bald = Character("Bald Head")
define pet1 = Character("Teacher Pet 1")
define pet2 = Character("Teacher Pet 2")
define cat = Character("Cat Demon")

define boy = Character("Boy")


image knife = im.FactorScale("images/knife/knife.png", 0.5)
image laughknife = im.FactorScale("images/knife/closedeyesknife.png", 0.5)
image nervousknife1 = im.FactorScale("images/knife/smswknife.png", 0.5)
image sparkleknife = im.FactorScale("images/knife/sparkleknife.png", 0.5)
image smileknife = im.FactorScale("images/knife/smileknife.png", 0.5)
image shockknife = im.FactorScale("images/knife/eyesknife.png", 0.5)
image nervousknife2 = im.FactorScale("images/knife/nervousknife.png", 0.5)
image teethknife = im.FactorScale("images/knife/teethknife.png", 0.5)
image eyesmouthknife = im.FactorScale("images/knife/eyesmouthknife.png", 0.5)
image toastknife = im.FactorScale("images/knife/toastknife.png", 0.5)

image fish = im.FactorScale("images/fish/fish.png", 0.5)
image sadfish = im.FactorScale("images/fish/sadfish.png", 0.5)
image shockedfish = im.FactorScale("images/fish/shockedfish.png", 0.5)
image confusedfish = im.FactorScale("images/fish/confusedfish.png", 0.5)
image tomatofish = im.FactorScale("images/fish/gapedfish.png", 0.5)
image blushfish = im.FactorScale("images/fish/blushfish.png", 0.5)
image wetfish = im.FactorScale("images/fish/wetfish.png", 0.5)
image wetfishtalk = im.FactorScale("images/fish/wetfishtalk.png", 0.95)


image tree = im.FactorScale("images/tree/tree.png", 0.95)
image madtree = im.FactorScale("images/tree/madtree.png", 0.95)
image shoetree = im.FactorScale("images/tree/shoetree.png", 0.95)
image shocktree = im.FactorScale("images/tree/shocktree.png", 0.95)

image toast = "toast.png"
image demoncat = im.FactorScale("demoncatirl.png", 0.6)

image white = '#FFF'
image black = "#000"


image walkschool = "images/background/walkschool.jpg"
image unwalkschool = im.Grayscale("images/background/walkschool.jpg")
image bedroom = "images/background/bedroom.jpg"
image bioclass = "images/background/bioclass.png"
image bio2 = "images/background/bio2.png"
image nurseoffice = "images/background/nurseoffice.png"
image demon = "images/background/demoncat.png"
image stairs = "images/background/stairs.png"
image ocean = "images/background/ocean.png"
image fishing = "images/background/fishing.png"


define vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
define hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)
define fade = Fade(0.5, 0.0, 0.5)
define fasterfade = Fade(1.5, 0.0, 0.5, color="#fff")
define whitefade = Fade(0.5, 0.0, 0.5, color="#fff")


define slideawaydown = CropMove(2.0, "slideawaydown")
define pushdown = PushMove(1.0, "pushdown")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show bedroom with fade
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue

    "It’s a bright, sunny day. The birds are chirping and you feel the warm rays of the sun hit you…"
    "Until you realize that you overslept."
    show bedroom with vpunch 
    you '"AHHHH!!!"'
    you '"I can’t believe I’m late for my first day of high school! I need to brush my teeth, brush my hair, wash my face, do my makeup, get dressed, and eat breakfast in 5 minutes!!"'

    menu: 
        "What should I do?"

        "Do all the above":
            show unwalkschool with fade
            "You were late to school. You got expelled, and then your parents disowned you. You got robbed after being homeless on the streets, dying of sunburn. "
            "Congratulations, you died within 5 lines of dialogue!"
            "Ending #1: Late"

            return 

        "Get dressed and brush teeth at the same time before grabbing toast":
            you '"Bye mom! I’m going now!"'
            hide bedroom with fade
                      
            # change scene 
   
    show walkschool with fade
    "I quickly ran out with toast in my mouth, grabbing my bag hastily. The wind brushed my hair as I sprinted as fast as I possibly could until…"
    show walkschool with vpunch
    "BAM!!" 
  

    you '“Ow… I’m so sorry–”'
    show toastknife at truecenter 
    'I gasped with horror, my toast flinging out of my mouth and splatooning onto a handsome boy’s face.'
    'I couldn’t believe who it was.'
    hide toastknife
    show knife at truecenter 
    you '“C-C-Cane Kn-Knight?!”'
    hide knife 
    show sparkleknife at truecenter 
    knife '"Are you okay, miss?"'
    "Cane Knight. An upperclassman in high school, known throughout our city for being extremely handsome, intelligent, and chivalrous."
    "Though he seems to be perfect in nearly every aspect, he wasn’t particularly close to anyone…"
    hide sparkleknife
    show knife at truecenter
    you '“I-I’m so sorry! I’m okay.”'
    

    menu:
        knife '“Do you want your toast back?”'

        "Yes":
                you '“Yes! No! I mean, you can keep it– wait what?”'
                hide knife
                show laughknife at truecenter
                "Cane lets out a small chuckle, handing the toast back."
        
        "No thanks":
            hide laughknife      
            knife '"Okay"'
            show toast with zoominout
            show toast at truecenter
            show toast at Move ((0.5, -1.0), (0.5, 8.0), 20.0, xanchor = 0.5, yanchor=0)
            show white with fade      

            "I saw my life flash before my eyes, the sheer force of the toast taking away my life."
            "Ending #2: You're Toast."

            return

    hide laughknife
    show knife at truecenter 
    you '“I’m so sorry again... please, take my handkerchief.”'
    knife'“It’s okay, thank you…?”'

    define pov = Character("[povname]")
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

    knife '"Thank you [povname]. Are you heading to Prince Academy of Arts High School as well?"'
    you '“Y-yes!”'
    hide knife
    show sparkleknife
    show sparkleknife at truecenter
    "Me and Cane bend down and attempt to grab all of our fallen belongings. My heart is racing from being in close proximity to Cane."
    "I breathed a sigh of relief when I saw the last book. I reached out to grab it and then.."
    you'“OH MY GOSH, I’M SO SORRY!”'
    "I yelped out in shock and embarrassment as our hands touched for 2 seconds straight. I shyly stared at him, flustered from our accidental hand touch."
    hide sparkleknife
    show shockknife at truecenter 
   

    menu: 
        knife '“Are you okay? I see your face heating up to 100 degrees fahrenheit.. Oh my–”'

        "Yes":
            hide shockknife
            show smileknife at truecenter
            "Your face was 100 degrees fahrenheit. You are in fact not okay."
            "Liars will always get their karma."
            #screen flash white and fade to black 
            show white with fasterfade
            
            "Lightning strikes and you die"
            return

        "No":
            image black = "#000"
            hide bedroom 
            show black with fade
            "I passed out."

            #change scene 
            hide shockknife  
            hide walkschool 

    
    show nurseoffice with fade
    nurse '“Hello. You’re finally awake!”' 
    you '“Wh-what… happened?”'
    nurse '“Your boyfriend carried you here and left to go to the library. The tall one with brown hair. You were passed out. Are you alright now?”'
    you '“B-b-boyfriend?!”'
    "My face heated up again. Cane carried me here?"
    nurse '“Well, whatever the case, you should get going to class if you’re recovered. Your second period is starting soon. According to your schedule, you should have… biology in five minutes.”'
    you '“Okay, thank you very much!”'
    "I grabbed my bag and rushed out."

    hide nurseoffice with fade
    show bioclass with fade
    "I panted, nearly out of breath from running."
    "Where should I sit?" 

    call screen classroom

    label Drool:
        show bioclass
        "There is drool all over the table"
        drooling '"Ehehehe..."'
        drooling '"ZZzZzzZ"'
        menu:
            "Should I sit here?"
            
            "Yes":
                "As I sat next to her, my skin began to burn."
                you '"Her drool is burning me. Why is it so acidic?!"'
                "I felt my consciousness slip..."
                show white with fade
                "Congratulations, you died from acidic drool from a NPC!"
                "Ending #3: Drool"
                return

            "No":
                "Yeah... let's not. That's gross."
                "What idiot would actually sit there?"
                call screen classroom

        return 
        
    

    label slaygirl: 
        show bioclass 
        girl '"UGH. YOU WOULD NEVER BELIEVE THE SUMMER I HAD."'
        boy '"Oh no. Tell me about it girl."'
        girl '"The guy I was dating joined some tree cutting cult... like what the heck?"'
        boy '"Girl, you dodged a bullet."'
        "They seem busy..."
        call screen classroom
        return 


    label twogirls:
        show bioclass
        girl1 '"Girl, I think my nose crooked"'
        girl2 '"See, I told you it was."'
        girl1 '"Okay? And your eyes are so far apart that they are divorced."'
        girl2 '"Your forehead reaches Mars."'
        girl1 '"This is why your mom left you."'
        "Maybe I shouldn't bother them..."
        call screen classroom
        return

    label teacherpet:
        show bioclass
        pet1 '"What did YOU do over the summer?"'
        pet2 '"I built a space rocket that flies over Mars for FASTFA. Not much."'
        pet1 '"Lame. I actually built a robot to slap liars in the face."'
        pet2 '"Wait, wha--"'
        "SMACK!!"
        "I'm not getting involved in that."
        call screen classroom
        return

    label stretch:
        show bioclass
        boy '"OARGHHHBH"'
        "He looks like he wants to sleep. The person next to him is already passed out."
        call screen classroom
        return

    label couple:
        show bioclass
        girl '"Would you still love me if I was a worm?"'
        boy '"Of course I would."'
        girl '"Then, why were you holding hands with that girl?"'
        boy '"She came up to me. I tried dodging but she kept bugging me."'
        girl '"Well then why did you breath the same air as her?"'
        boy '"..."'
        girl '"Hmph. You hate me."'
        "I don't want to be involved in this soap opera..."
        call screen classroom

    label cat:
        show bioclass 
        unknown '"Meow"'
        boy '"Shhh! Be quiet, I was not supposed to bring you here."'
        unknown '"Meow, meow."'
        menu:
            "Should I sit here?"
            
            "Yes":
                "As I was about to sit down on the chair next to the boy, there was a sudden flash."
                hide bioclass
                show demon with fade
                show demoncat at truecenter
                menu:
                    cat '"You dare try to sit on me? You puny pathetic human."'

                    "Yes":
                        cat '"How dare you!"'
                        "I felt a crushing weight on me."
                        "Crunch!"
                        show demoncat with zoominout
                        show demoncat with hpunch

                    "No":
                        cat '"How dare you lie to me?"'
                        "I felt a crushing weight on me."
                        "Crunch!"
                        show demoncat with zoominout
                        show demoncat with hpunch

                "I felt my consciousness slip..."
                show white with fade
                "Ending #4: Cat Demon"
                return

            "No":
                "I think there's a cat in that seat..."
                "I don't want to hurt the poor kitty."
                call screen classroom
                return 


    label bald:
        bald '"The weather is wonderful outside! What a wonderful day to be hairless!"'
        boy '"What the heck is wrong with this bald dude..."'
        boy '"Is he even a student here...?"'
        bald '"Come, young one! Join me in my baldness!!"'
        boy '"NO."'
        menu:
            "Should I interfere?"

            "Yes":
                "Congratulations, you now have a bald head too."
                "Your parents disown you for being bald. You end up homeless and died from baldness."
                "Ending #5: BALD"
                return

            "No":
                "I don't want to be bald."
                "Yeah, I'll find another seat."
                call screen classroom
                return 

    label nextbald:
        bald '"The weather is wonderful outside! What a wonderful day to be hairless!"'
        boy '"What the heck is wrong with this bald dude..."'
        boy '"Is he even a student here...?"'
        bald '"Come, young one! Join me in my baldness!!"'
        boy '"NO."'
        menu:
            "Should I interfere?"

            "Yes":
                "Congratulations, you now have a bald head too."
                "Your parents disown you for being bald. You end up homeless and died from baldness."
                "Ending #5: BALD"
                return

            "No":
                "I don't want to be bald."
                "Yeah, I'll find another seat."
                call screen classroom
                return 

            
        label fish: 
            show bioclass
            "I think I can sit here."
            show bio2 with fade
        
            

   
    show fish 
    "As I took my seat, I glanced over to the boy next to me."
    "His fluffy pink hair nestled on his head, his seafoam-colored eyeballs peeking through. His oversized raggedy, dull kelp-colored jacket made him look like he came from the ocean."
    "In fact, he smelled strangely like seawater. And…"
    you '“Is that a water bucket?”'
    hide fish 
    show tomatofish
    unknown '“Y-y-yes?!”'
    you '“That’s… interesting. What do you need it for?”'
    unknown '“U-uhm…”'
    hide tomatofish
    teacher '“Welcome to biology, everyone. For introductions, please get out a piece of paper and write down three fun facts and something you did over the summer."'
    teacher '"Share it with the person next to you and then we will read these out loud in about ten minutes.”'
    "I guess I should start writing…"

    define fact1 = Character("[fact1]")
    python:
        fact1 = renpy.input("One fun fact about me is:")
        fact1 = fact1.strip()
    define fact2 = Character("[fact2]")
    python:
        fact2 = renpy.input("A second fun fact about me is:")
        fact2 = fact2.strip()    
    define fact3 = Character("[fact3]")
    python:
        fact3 = renpy.input("Third fun fact about me is:")
        fact3 = fact3.strip()


    "By the time I finished, the boy next to me finished writing as well."
    show tomatofish
    unknown '“Y-y-y-you c-can g-go first..!”'
    you '“My name is [povname]. Three fun facts about me are..."'
    you '"[fact1]"'
    you '"[fact2]"'
    you '"and [fact3]"'
    you '"And something I did over the summer…”'
    #flashback
    hide bioclass
    hide tomatofish
    show ocean with fade
    hide bio2
    "Summer. July 26 Year 2020\nThe bright sun beamed harshly on my skin. Combined with the humid air, the summer heat was killing me."
    dad '“Let’s go fishing!”'
    you '“Sure Dad.”'
    "As soon as we got to the fishing site, my dad spotted his friends and left me alone. I grabbed the fishing rod and attempted to fish on my own."
    "After waiting impatiently for 30 minutes, the fishing rod finally moved. I could feel it. This one was heavy."
    "I used my entire body to pull up the fish, struggling under the summer heat."
    show ocean with vpunch
    "!!!!!"
    hide ocean 
    show fishing with whitefade
    show fishing with hpunch
    you '“I CAUGHT IT!”'
    "It was a humongous pink fish with glittering blue eyes. A very unusual color. I locked eyeballs with the fish in awe."
    you '“I gotta tell my dad I caught a super rare, big fish!”'
    you '“DAD, LOOK WHAT I CAUGHT!”'
    dad '“WHAT?”'
    hide fishing
    show ocean 
    you '“IT’S A HUGE, PINK… huh? Where did it go?”'
    hide tomatofish
    hide ocean 
    you '“And that’s what happened.”'
    show bio2 with fade
    show shockedfish at truecenter
    you "The boy gaped at me in shock."
    unknown '“Th-th-that’s interesting to know…”'
    you '“How about you?”'
    hide shockedfish
    show confusedfish 
    fish '“M-my name is Prince Salaman. I like cl-cleaning up the pollution in the ocean, eating kelp, and most importantly… I love–”'
    #screen shake? sound effect?
    hide confusedfish
    show wetfish at truecenter 
    show bio2 with vpunch
    "Blub blub blub"
    hide wetfish
    show wetfishtalk
    fish '“W-Water…”'
    hide wetfishtalk
    show wetfish 
    "Did he just dunk his head in water?"
    you '“Oh! That’s nice!”' 
    "I wiped the seawater from my face."
    fish '“Y-you think so?”'
    you '“Yeah…?”'
    fish '“Th-Thank you…!”'
    you '“Uh… so what did you do over the summer?"'
    hide wetfish
    show wetfishtalk
    fish '“I swam away from home.”'
    you '"Huh?"'
    you '“You swam? Away…?”'
    teacher '“Time’s up, everyone! We will now begin the lesson.”'
    "My interaction with Prince Salaman stuck in my mind. I zoned out until the end of class, the salty smell of water lingered in the air even as I left."

    #change scene 
    hide wetfishtalk
    hide bio2 with fade
    show stairs with fade
    "It’s finally near the end of the day. I yawned from sheer exhaustion."
    "I was too excited last night to sleep properly…"
    "I sluggishly walked down the stairs, when all of a sudden…"
    show stairs with hpunch
    you '“AHHHH!!”'
    "My shoe flung off my foot, but I didn’t have time to think about it."
    unknown '“Oof.”'
    "I felt big, strong, muscular arms wrap around me, catching me before I could plummeted on head. I looked up to see who it was."
    you '“Th-thank y–”'
    show shoetree at truecenter 
    "SHPACK!!"
    "I gasped in horror. My shoe smacked him square in his face. When my shoe peeled off his face, my jaw dropped even further."
    you '“B-Brunt?”'
    hide shoetree
    show tree at truecenter
    "Brunt Oak Woods was notorious in our grade since middle school. He often got into fights with other people and was known for his short temper." 
    "People say he has connections with gang members and is regularly involved in crimes. However, more recently, people say that he skips class to go to the rooftop."
    "Truthfully, I was terrified of him as well. My heart pounded loudly in my chest in fear."
    hide tree
    show madtree at truecenter
    tree '“Tch. Watch where you’re going.”'
    you '“I-I’M SO SORRY!”'
    "He just glared at me."
    "In response, I immediately ran off, leaving my stinky shoe with him."
    hide madtree
    show shocktree at truecenter 
    tree '“Hey, wait!”'
    "It was too late. I kept running away, fearing for my life."
    "Just like that, my first day of high school came to an end"
    hide shocktree
    hide stairs with fade

    #change scene 
    show bedroom with fade 
    "The sun rose once again today and I didn’t wake up late, thankfully."
    "Today, I took my time getting ready. Feeling much more refreshed and energized than yesterday, I set off to school."
    hide bedroom with fade
    show walkschool with fade
    "The day passed by in a blur once again. My last class ended much earlier than expected, giving me an early dismissal."

    menu: 
            "What do you want to do?"

            "Go to the rooftop": 
                "bye"
            "Go to the swimming pool":
                "bye"
            "Go to study hall/library":
                "bye"







    # This ends the game.

return
