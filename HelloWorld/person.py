import pygame, ctypes, time, random
from pydub import AudioSegment
pygame.init()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
win = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)

clock = pygame.time.Clock()








def setupSpeech():
    letters = [
    "a", "b", "c", "d", "e", "f", "g", "h",
    "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x",
    "y", "z"
    ]

    otherSounds = ["ch","sh","ph","th","wh","oo"]

    return letters, otherSounds

def speech(lettters,otherSounds,text,voiceType):
    
    soundsList = []
    
    for i in range(len(text)):
        if text[i].lower() in letters:
            soundsList.append(AudioSegment.from_wav(f"sounds/{voiceType}/{text[i].lower()}.wav"))
        elif text[i] == " ":
            soundsList.append(AudioSegment.from_wav("sounds/space.wav"))
        elif text[i] == ",":
            for i in range(3):
                soundsList.append(AudioSegment.from_wav("sounds/space.wav"))

    soundsList = soundsList[::-1]

    combined_sounds = None

    num = 0
    for i in soundsList:
        
        if num != 0:
            combined_sounds = i + AudioSegment.from_wav("finish.wav")
            combined_sounds.export("finish.wav", format="wav")
        
        else:
            combined_sounds = i
            combined_sounds.export("finish.wav", format="wav")
        
        num += 1

    sound = AudioSegment.from_file("finish.wav")
    def speed_change(sound, speed=1.0):
        sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
            "frame_rate": int(sound.frame_rate * speed)
        })

        return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


    fast_sound = speed_change(sound, 2.6)

    fast_sound.export("finish.wav", format="wav")

    sound = pygame.mixer.Sound("finish.wav")
    return sound












def createText(win,text,font,colour,size):
    
    fontFormat = pygame.font.SysFont(font,size)

    message = fontFormat.render(text,True,colour)

    return message


def get_display_name():
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = 3

    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)

    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    return nameBuffer.value

def displayMessage(win,letters,otherSounds,voiceType,text,timer,backgroundColour = (255,255,255),textColour = (0,0,0),textNum = 0):


    text2 = text[:textNum]
    
    message = createText(win,text2,"bahnschrift",textColour,40)
    
    win.fill(backgroundColour)
    
    win.blit(message,(win.get_width()/2 - message.get_width() / 2, win.get_height()/2 - message.get_height() / 2))
    
    pygame.display.update()

    if textNum <= len(text)-1:
        if text[textNum].lower() in letters:
            sound = pygame.mixer.Sound(f"sounds/{voiceType}/{text[textNum].lower()}.wav")
            pygame.mixer.Sound.play(sound)

    time.sleep(timer)
    
    if text2 != text:
        textNum += 1
        displayMessage(win,letters,otherSounds,voiceType,text,timer,backgroundColour,textColour,textNum)

def displayMessagePress(win,letters,otherSounds,voiceType,text,timer,backgroundColour = (255,255,255),textColour = (0,0,0),textNum = 0):
    pressed = False
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            pressed = True
    
    if pressed == False:
        text2 = text[:textNum]

        message = createText(win,text2,"bahnschrift",textColour,40)

        win.fill(backgroundColour)

        win.blit(message,(win.get_width()/2 - message.get_width() / 2, win.get_height()/2 - message.get_height() / 2))

        pygame.display.update()

        if textNum <= len(text)-1:
            if text[textNum].lower() in letters:
                sound = pygame.mixer.Sound(f"sounds/{voiceType}/{text[textNum].lower()}.wav")
                pygame.mixer.Sound.play(sound)
        
        if pressed == False:
            time.sleep(timer)
            if text2 != text:
                textNum += 1
                pressed = displayMessagePress(win,letters,otherSounds,voiceType,text,timer,backgroundColour,textColour,textNum)
    
    return pressed



letters, otherSounds = setupSpeech()


time_start = time.clock()   
displayMessage(win,letters,otherSounds,"male2","Hello?",0.3)
time.sleep(1)
displayMessage(win,letters,otherSounds,"male2","Can you hear me?",0.05)
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2","Mhhhh...",0.1)
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2","It says you can see me",0.05)
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2","Oh well that will have to do",0.05)
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2","Soooo",0.12)
time.sleep(1)
displayMessage(win,letters,otherSounds,"male2","Who are you?",0.2)
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2",f"It says here you're {get_display_name()}...",0.06)
time.sleep(3)
displayMessage(win,letters,otherSounds,"male2","Or is that someone else?",0.05)
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2","Okay I think we have to establish some communication here",0.05)
time.sleep(1)
displayMessage(win,letters,otherSounds,"male2",f"We've already been here for {time.clock()-time_start} seconds...",0.05)
time.sleep(1.5)
displayMessage(win,letters,otherSounds,"male2","Right, I'm going to put a Y and an N on the screen",0.05)
time.sleep(1)
displayMessage(win,letters,otherSounds,"male2","when you want to say yes just simply press Y",0.05)
time.sleep(1)
displayMessage(win,letters,otherSounds,"male2","and when you want to say no just simply press N",0.05)
time.sleep(2)
displayMessage(win,letters,otherSounds,"male3","You got it?",0.03)
time.sleep(3)
displayMessage(win,letters,otherSounds,"male2","Oh yeah the Y and N needs setting up first",0.03)
time.sleep(1)
displayMessage(win,letters,otherSounds,"male2","One second...",0.1)
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2","Don't press anything please",0.04)
time.sleep(2)

textNum = 0
textList = ["That goes there","Oh that shouldn't be like that","Put this here","God it stinks back here","Shouldn't be too much longer","Where did that Y go?","Thank the lord you haven't pressed any buttons","Hmmm","No that bits all wrong","Oh I had it the wrong way around","Left side goes first","I'm nearly there","Erm...","You're doing great carry on doing nothing","As long as you don't press anything I'm happy","I'm not sure about that one","Should that be buzzing like that!","Nearly, nearly...","Maybe that's not the way to do it","...","Yes, yes, must be like that", "What does the manual say again","This side seems to be in Portuguese","If only this screwdriver was magnetic"]
random.shuffle(textList)
pressed = False
while pressed == False:
    
    pressed = displayMessagePress(win,letters,otherSounds,"male2",textList[textNum],0.05)
    
    if textNum < len(textList)-1:
        textNum += 1 
    else:
        textNum = 0
    
    if pressed == False:
        time.sleep(2.7)

displayMessage(win,letters,otherSounds,"male2","",0.1,(0,0,0))
time.sleep(3)
displayMessage(win,letters,otherSounds,"male2",". . .",0.5,(0,0,0),(20,20,20))
time.sleep(2)
displayMessage(win,letters,otherSounds,"male3","Did you press something?!",0.1,(0,0,0),(20,20,20))
time.sleep(1.5)
displayMessage(win,letters,otherSounds,"male2","Fuck... where's the light switch?",0.04,(0,0,0),(20,20,20))
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2","This will have to do for now",0.04,(0,0,0),(255,255,255))
time.sleep(1.5)
displayMessage(win,letters,otherSounds,"male2","Right I'm going to assume that you pressed that by accident",0.04,(0,0,0),(255,255,255))
time.sleep(2)
displayMessage(win,letters,otherSounds,"male2","Luckily for you I was basically done",0.05,(0,0,0),(255,255,255))
time.sleep(1)
displayMessage(win,letters,otherSounds,"male2","All we gotta do it turn it on",0.05,(0,0,0),(255,255,255))
time.sleep(1)
displayMessage(win,letters,otherSounds,"male2","three...",0.05,(0,0,0),(255,255,255))
time.sleep(0.5)
displayMessage(win,letters,otherSounds,"male3","two...",0.05,(0,0,0),(255,255,255))
time.sleep(0.5)
displayMessage(win,letters,otherSounds,"male2","one...",0.05,(0,0,0),(255,255,255))
time.sleep(0.5)
text = ""
for i in range(5):
    displayMessage(win,letters,otherSounds,"male3",text,0.05,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

