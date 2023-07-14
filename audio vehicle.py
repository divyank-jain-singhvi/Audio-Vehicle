
import pyttsx3
import speech_recognition as sr
def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query
p=take_commands()
k,e,h,q,r,U = 0,0,0,0,0,0
while p == 'expert player':                                                                              # change password
    Speak('''You can select your vehicle from the following option:-
1) car
2) bike
3) truck
4) scooter
5) plane
6) cycle''')
    i = take_commands()
    if i == 'kar':                                                                                   # car control
        Speak('you can select car company from the following option:-')
        print('''    1) Lamborghini
    2) Ferrari
    3) Mercedes
    4) BMW
    5) Volkswagen
    6) Indigo
    7) Mahindra Thar
    8) Hyundi i20
    9) Kia Sonet
   10) Tata Altroz
   11) Maruti Swift
   12) Toyota Fortuner
   13) MG Hactor
   14) Hyundi Venue
   15) Nissa Magnite 
   16) Mahindra Scorpio
   17) Maruti Vitara Brezza
   18) Tata Nexon
   19) Mahindra Bolero
   20) Toyota Innova''')
        U = int(take_commands())
        if U > 20 :
            Speak('this number does not exist 1st option is selected')
        elif U < 1:
            Speak('this number does not exist 1st option is selected')
        else:
            Speak('car has been selected')
            print()
        Speak('''start   : To start the car engine.
off     : To off the car engine.
forward : To move your car in forward direction.
reverse : To move your car in backward direction.
left    : To move your car in left direction.
right   : To move your car in right direction.
quit    : To exit game.''')
    elif i == 'bike':                                                                               # bike control
        Speak('you can select bike company from the following option:-')
        print('''1) TRK 502
    2) Speed Triple 1200
    3) Scrambler Icon
    4) Classic 350
    5) Meteor 350
    6) YZF R15 V3
    7) Bullet 350
    8) FZ S FI
    9) MT 15
   10) Pulsar 125
   11) SP 125
   12) Hness CB350
   13) Splender Plus 
   14) Pulsar 150
   15) Passion pro
   16) Apachi RTR 160 4V
   17) Dhoom
   18) Shine
   19) Hornet 2.0
   20) Himalayan''')
        U = int(take_commands())
        if U > 20 :
            Speak('this number does not exist 1st option is selected')
        elif U < 1:
            Speak('this number does not exist 1st option is selected')
        else:
            Speak('bike has been selected')
            print()
        Speak('''start   : To start the bike engine.
off     : To off the bike engine.
forward : To move your bike in forward direction.
reverse : To move your bike in backward direction.
left    : To move your bike in left direction.
right   : To move your bike in right direction.
quit    : To exit game.''')
    elif i == 'truck':                                                                             # truck control
        Speak('you can select truck company from the following option:-')
        print('''1) Ford F-150
    2) Ford Ranger
    3) Nissan Titan
    4) Ram 1500
    5) Toyota Tundra
    6) Chevrolrt Silveradio 1500
    7) Nissan Frontier
    8) GMC canyon
    9) Chevrolet Colorado
   10) Honda Ridgeline''')
        U = int(take_commands())
        if U > 10 :
            Speak('this number does not exist 1st option is selected')
        elif U < 1:
            Speak('this number does not exist 1st option is selected')
        else:
            Speak('truck has been selected')
            print()
        Speak('''start   : To start the truck engine.
off     : To off the truck engine.
forward : To move your truck in forward direction.
reverse : To move your truck in backward direction.
left    : To move your truck in left direction.
right   : To move your truck in right direction.
quit    : To exit game.''')
    elif i == 'scooter':                                                                           # scooter control
        Speak('you can select scooter company from the following option:-')
        print('''1) Honda Activa 6G
    2) Honda Dio
    3) Suzuki Access 125
    4) Suzuki Burgman Street
    5) Hero Pleasure Plus
    6) Yamaha Fascino 125
    7) TVS jupiter
    8) TVS NTORQ 125
    9) Honda Activa 125
   10) TVS XL 100
   11) Ather 450X
   12) Bajaj Chetak
   13) Hero Electric Optima LA
   14) Yahama Ray-ZR125
   15) Honda Grazia
   16) Hero Maestro Edge 125
   17) Ather 450
   18) TVS SCooty Pep Plus
   19) Hero Electric Flash
   20) Aprilia SXR 160''')
        U = int(take_commands())
        if U > 20 :
            Speak('this number does not exist 1st option is selected')
        elif U < 1:
            Speak('this number does not exist 1st option is selected')
        else:
            Speak('scooter has been selected')
            print()
        Speak('''start   : To start the scooter engine.
off     : To off the scooter engine.
forward : To move your scooter in forward direction.
reverse : To move your scooter in backward direction.
left    : To move your scooter in left direction.
right   : To move your scooter in right direction.
quit    : To exit game.''')
    elif i == 'plane':                                                                               # plane control
        Speak('you can select plane company from the following option:-')
        print('''1) Wright Flyer
    2) Supermarine Spitfire
    3) Boeing787
    4) Lockheed SR-71 BLackbird
    5) Cirrus SR22
    6) Learet 23
    7) Lockheed C-130
    8) Douglas DC-3
    9) Bleriot 11
   10) Cessan 172
   11) Boeing B-29 Superfortress
   12) Gulfstream G500
   13) Boeing 747
   14) Bell x-1
   15) Spirit of St. Louis
   16) Rutan VariEze
   17) Lockheed Martin F-35 Lightning 2
   18) Airbus A320
   19) Lockheed Constellation
   20) General Atomics MQ-1 Predator''')
        U = int(take_commands())
        if U > 20 :
            Speak('this number does not exist 1st option is selected')
        elif U < 1:
            Speak('this number does not exist 1st option is selected')
        else:
            Speak('plane has been selected')
            print()
        Speak('''start   : To start the plane engine.
off     : To off the car engine.
forward : To move your plane in forward direction.
reverse : To move your plane in backward direction.
left    : To move your plane in left direction.
right   : To move your plane in right direction.
quit    : To exit game.''')
    if i == 'cycle':                                                                     # cycle control
        Speak('you can select cycle company from the following option:-')
        print('''1) 3T
    2) 6ku
    3) Alan Bike
    4) Alchemy Bikes
    5) Alex Singer
    6) All-City
    7) Allied Cycle Works
    8) Altruiste Bikes
    9) Argon 18
   10) Hero Street
   11) Avanti Bicycles
   12) Basso
   13) BAttaglin
   14) Baum
   15) Beiou
   16) Beone
   17) BH
   18) Bianchi
   19) Bike Friday
   20) Chesini''')
        U = int(take_commands())
        if U > 20 :
            Speak('this number does not exist 1st option is selected')
        elif U < 1:
            Speak('this number does not exist 1st option is selected')
        else:
            Speak('cycle has been selected')
            print()
        Speak('''start   : To open the lock of cycle.
off     : To close the lock of cycle.
forward : To move your cycle in forward direction.
reverse : To move your cycle in backward direction.
left    : To move your cycle in left direction.
right   : To move your cycle in right direction.
quit    : To exit game.''')
    while i == 'kar':                                                                               # car code
        x = take_commands()
        if x == 'start':
            if k == 0:
                Speak('Your car engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                Speak('your car engine is already started.')
        elif x == 'of':
            if q == 1:
                Speak('Your car engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                Speak('your car engine is already off !!')
        elif x == 'forward':
            if k == 1:
                Speak('Your car is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                Speak('your car is already moving forward')
            else:
                Speak('please start your car engine first')
        elif x == 'reverse':
           if h == 1:
                Speak('Your car is in reverse gear.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                Speak('reverse gear is already applied')
           else:
                Speak('please start your car engine first')
        elif x == 'left':
            if e == 1:
                Speak('Your car is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                Speak('your car is already moving in left direction !!')
            else:
                Speak('please start your car engine first')
        elif x == 'right':
            if r == 1:
                Speak('Your car is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                Speak('your car is already moving in right direction')
            else:
                Speak('please start your car engine first')
        elif x == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            Speak('Game over')
            print()
            print()
            break
        else:
            Speak("invalid command !!")
    while i == 'bike':                                                                      # bike code
        y = take_commands()
        if y == 'start':
            if k == 0:
                Speak('Your bike engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                Speak('your bike engine is already started.')
        elif y == 'of':
            if q == 1:
                Speak('Your bike engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                Speak('your bike engine is already off !!')
        elif y == 'forward':
            if k == 1:
                Speak('Your bike is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                Speak('your bike is already moving forward')
            else:
                Speak('please start your bike engine first')
        elif y == 'reverse':
           if h == 1:
                Speak('Your bike is moving backward.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                Speak('your bike is already moving backward.')
           else:
                Speak('please start your bike engine first')
        elif y == 'left':
            if e == 1:
                Speak('Your bike is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                Speak('your bike is already moving in left direction !!')
            else:
                Speak('please start your bike engine first')
        elif y == 'right':
            if r == 1:
                Speak('Your bike is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                Speak('your bike is already moving in right direction')
            else:
                Speak('please start your bike engine first')
        elif y == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            Speak('Game over')
            print()
            print()
            break
        else:
            Speak("invalid command !!")
    while i == 'scooter':                                                                   # scooter code
        z = take_commands()
        if z == 'start':
            if k == 0:
                Speak('Your scooter engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                Speak('your scooter engine is already started.')
        elif z == 'of':
            if q == 1:
                Speak('Your scooter engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                Speak('your scooter engine is already off !!')
        elif z == 'forward':
            if k == 1:
                Speak('Your scooter is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                Speak('your scooter is already moving forward')
            else:
                Speak('please start your scooter engine first')
        elif z == 'reverse':
           if h == 1:
                Speak('your scooter is moving backard.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                Speak('your scooter is alerady moving backward.')
           else:
                Speak('please start your scooter engine first')
        elif z == 'left':
            if e == 1:
                Speak('Your scooter is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                Speak('your scooter is already moving in left direction !!')
            else:
                Speak('please start your scooter engine first')
        elif z == 'right':
            if r == 1:
                Speak('Your scooter is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                Speak('your scooter is already moving in right direction')
            else:
                Speak('please start your scooter engine first')
        elif z == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            Speak('Game over')
            print()
            print()
            break
        else:
            Speak("invalid command !!")
    while i == 'truck':                                                                     # truck code
        w = take_commands()
        if w == 'start':
            if k == 0:
                Speak('Your truck engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                Speak('your truck engine is already started.')
        elif w == 'of':
            if q == 1:
                Speak('Your truck engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                Speak('your truck engine is already off !!')
        elif w == 'forward':
            if k == 1:
                Speak('Your truck is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                Speak('your truck is already moving forward')
            else:
                Speak('please start your truck engine first')
        elif w == 'reverse':
           if h == 1:
                Speak('Your truck is in reverse gear.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                Speak('reverse gear is already applied')
           else:
                Speak('please start your truck engine first')
        elif w == 'left':
            if e == 1:
                Speak('Your truck is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                Speak('your truck is already moving in left direction !!')
            else:
                Speak('please start your truck engine first')
        elif w == 'right':
            if r == 1:
                Speak('Your truck is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                Speak('your truck is already moving in right direction')
            else:
                Speak('please start your truck engine first')
        elif w == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            Speak('Game over')
            print()
            print()
            break
        else:
            Speak("invalid command !!")
    while i == 'plane':                                                                     # plane code
        c = take_commands()
        if c == 'start':
            if k == 0:
                Speak('Your plane engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                Speak('your plane engine is already started.')
        elif c == 'of':
            if q == 1:
                Speak('Your plane engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                Speak('your plane engine is already off !!')
        elif c == 'forward':
            if k == 1:
                Speak('Your plane is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                Speak('your plane is already moving forward')
            else:
                Speak('please start your plane engine first')
        elif c == 'reverse':
           if h == 1:
                Speak('Your plane is in reverse gear.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                Speak('reverse gear is already applied')
           else:
                Speak('please start your plane engine first')
        elif c == 'left':
            if e == 1:
                Speak('Your plane is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                Speak('your plane is already moving in left direction !!')
            else:
                Speak('please start your plane engine first')
        elif c == 'right':
            if r == 1:
                Speak('Your plane is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                Speak('your plane is already moving in right direction')
            else:
                Speak('please start your plane engine first')
        elif c == 'quit':
            Speak('Game over')
            k, e, h, q, r, = 0, 0, 0, 0, 0
            print()
            print()
            break
        else:
            Speak("invalid command !!")
    while i == 'cycle':                                                                               # cycle code
        v = take_commands()
        if v == 'start':
            if k == 0:
                Speak('Your cycle has been unlocked.')
                k,h,q,e = 1,1,1,1
            else:
                Speak('your cycle is already unlocked.')
        elif v == 'of':
            if q == 1:
                Speak('Your cycle has been locked.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                Speak('your cycle is already locked !!')
        elif v == 'forward':
            if k == 1:
                Speak('Your cycle is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                Speak('your cycle is already moving forward')
            else:
                Speak('please unlock your cycle first')
        elif v == 'reverse':
           if h == 1:
                Speak('now your cycle is moving backward.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                Speak('your cycle is already moving back')
           else:
                Speak('please unlock your cycle first')
        elif v == 'left':
            if e == 1:
                Speak('Your cycle is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                Speak('your cycle is already moving in left direction !!')
            else:
                Speak('please unlock your cycle first')
        elif v == 'right':
            if r == 1:
                Speak('Your cycle is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                Speak('your cycle is already moving in right direction')
            else:
                Speak('please unlock your cycle first')
        elif v == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            Speak('Game over')
            print()
            print()
            break
        else:
            Speak("invalid command !!")
else:
    Speak('Wrong password')
