k,e,h,q,r,U = 0,0,0,0,0,0
p = input('Password:')
while p == 'Xpert player':                                                                              # change password
    print('''You can select your vehicle from the following option:-
1) car
2) bike
3) truck
4) scooter
5) plane
6) cycle''')
    i = input('>')
    if i == 'car':                                                                                   # car control
        print('''you can select car company from the following option:-
    1) Lamborghini
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
        U = int(input('>'))
        if U > 20 :
            print('this number does not exist 1st option is selected')
        elif U < 1:
            print('this number does not exist 1st option is selected')
        else:
            print('car has been selected')
            print()
        print('''start   : To start the car engine.
off     : To off the car engine.
forward : To move your car in forward direction.
reverse : To move your car in backward direction.
left    : To move your car in left direction.
right   : To move your car in right direction.
quit    : To exit game.''')
    elif i == 'bike':                                                                               # bike control
        print('''you can select bike company from the following option:-
    1) TRK 502
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
        U = int(input('>'))
        if U > 20 :
            print('this number does not exist 1st option is selected')
        elif U < 1:
            print('this number does not exist 1st option is selected')
        else:
            print('bike has been selected')
            print()
        print('''start   : To start the bike engine.
off     : To off the bike engine.
forward : To move your bike in forward direction.
reverse : To move your bike in backward direction.
left    : To move your bike in left direction.
right   : To move your bike in right direction.
quit    : To exit game.''')
    elif i == 'truck':                                                                             # truck control
        print('''you can select truck company from the following option:-
    1) Ford F-150
    2) Ford Ranger
    3) Nissan Titan
    4) Ram 1500
    5) Toyota Tundra
    6) Chevrolrt Silveradio 1500
    7) Nissan Frontier
    8) GMC canyon
    9) Chevrolet Colorado
   10) Honda Ridgeline''')
        U = int(input('>'))
        if U > 10 :
            print('this number does not exist 1st option is selected')
        elif U < 1:
            print('this number does not exist 1st option is selected')
        else:
            print('truck has been selected')
            print()
        print('''start   : To start the truck engine.
off     : To off the truck engine.
forward : To move your truck in forward direction.
reverse : To move your truck in backward direction.
left    : To move your truck in left direction.
right   : To move your truck in right direction.
quit    : To exit game.''')
    elif i == 'scooter':                                                                           # scooter control
        print('''you can select scooter company from the following option:-
    1) Honda Activa 6G
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
        U = int(input('>'))
        if U > 20 :
            print('this number does not exist 1st option is selected')
        elif U < 1:
            print('this number does not exist 1st option is selected')
        else:
            print('scooter has been selected')
            print()
        print('''start   : To start the scooter engine.
off     : To off the scooter engine.
forward : To move your scooter in forward direction.
reverse : To move your scooter in backward direction.
left    : To move your scooter in left direction.
right   : To move your scooter in right direction.
quit    : To exit game.''')
    elif i == 'plane':                                                                               # plane control
        print('''you can select plane company from the following option:-
    1) Wright Flyer
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
        U = int(input('>'))
        if U > 20 :
            print('this number does not exist 1st option is selected')
        elif U < 1:
            print('this number does not exist 1st option is selected')
        else:
            print('plane has been selected')
            print()
        print('''start   : To start the plane engine.
off     : To off the car engine.
forward : To move your plane in forward direction.
reverse : To move your plane in backward direction.
left    : To move your plane in left direction.
right   : To move your plane in right direction.
quit    : To exit game.''')
    if i == 'cycle':                                                                     # cycle control
        print('''you can select cycle company from the following option:-
    1) 3T
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
        U = int(input('>'))
        if U > 20 :
            print('this number does not exist 1st option is selected')
        elif U < 1:
            print('this number does not exist 1st option is selected')
        else:
            print('cycle has been selected')
            print()
        print('''start   : To open the lock of cycle.
off     : To close the lock of cycle.
forward : To move your cycle in forward direction.
reverse : To move your cycle in backward direction.
left    : To move your cycle in left direction.
right   : To move your cycle in right direction.
quit    : To exit game.''')
    while i == 'car':                                                                               # car code
        x = input('>')
        if x == 'start':
            if k == 0:
                print('Your car engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                print('your car engine is already started.')
        elif x == 'off':
            if q == 1:
                print('Your car engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                print('your car engine is already off !!')
        elif x == 'forward':
            if k == 1:
                print('Your car is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                print('your car is already moving forward')
            else:
                print('please start your car engine first')
        elif x == 'reverse':
           if h == 1:
                print('Your car is in reverse gear.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                print('reverse gear is already applied')
           else:
                print('please start your car engine first')
        elif x == 'left':
            if e == 1:
                print('Your car is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                print('your car is already moving in left direction !!')
            else:
                print('please start your car engine first')
        elif x == 'right':
            if r == 1:
                print('Your car is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                print('your car is already moving in right direction')
            else:
                print('please start your car engine first')
        elif x == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            print('Game over')
            print()
            print()
            break
        else:
            print("invalid command !!")
    while i == 'bike':                                                                      # bike code
        y = input('>')
        if y == 'start':
            if k == 0:
                print('Your bike engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                print('your bike engine is already started.')
        elif y == 'off':
            if q == 1:
                print('Your bike engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                print('your bike engine is already off !!')
        elif y == 'forward':
            if k == 1:
                print('Your bike is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                print('your bike is already moving forward')
            else:
                print('please start your bike engine first')
        elif y == 'reverse':
           if h == 1:
                print('Your bike is moving backward.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                print('your bike is already moving backward.')
           else:
                print('please start your bike engine first')
        elif y == 'left':
            if e == 1:
                print('Your bike is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                print('your bike is already moving in left direction !!')
            else:
                print('please start your bike engine first')
        elif y == 'right':
            if r == 1:
                print('Your bike is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                print('your bike is already moving in right direction')
            else:
                print('please start your bike engine first')
        elif y == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            print('Game over')
            print()
            print()
            break
        else:
            print("invalid command !!")
    while i == 'scooter':                                                                   # scooter code
        z = input('>')
        if z == 'start':
            if k == 0:
                print('Your scooter engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                print('your scooter engine is already started.')
        elif z == 'off':
            if q == 1:
                print('Your scooter engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                print('your scooter engine is already off !!')
        elif z == 'forward':
            if k == 1:
                print('Your scooter is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                print('your scooter is already moving forward')
            else:
                print('please start your scooter engine first')
        elif z == 'reverse':
           if h == 1:
                print('your scooter is moving backard.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                print('your scooter is alerady moving backward.')
           else:
                print('please start your scooter engine first')
        elif z == 'left':
            if e == 1:
                print('Your scooter is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                print('your scooter is already moving in left direction !!')
            else:
                print('please start your scooter engine first')
        elif z == 'right':
            if r == 1:
                print('Your scooter is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                print('your scooter is already moving in right direction')
            else:
                print('please start your scooter engine first')
        elif z == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            print('Game over')
            print()
            print()
            break
        else:
            print("invalid command !!")
    while i == 'truck':                                                                     # truck code
        w = input('>')
        if w == 'start':
            if k == 0:
                print('Your truck engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                print('your truck engine is already started.')
        elif w == 'off':
            if q == 1:
                print('Your truck engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                print('your truck engine is already off !!')
        elif w == 'forward':
            if k == 1:
                print('Your truck is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                print('your truck is already moving forward')
            else:
                print('please start your truck engine first')
        elif w == 'reverse':
           if h == 1:
                print('Your truck is in reverse gear.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                print('reverse gear is already applied')
           else:
                print('please start your truck engine first')
        elif w == 'left':
            if e == 1:
                print('Your truck is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                print('your truck is already moving in left direction !!')
            else:
                print('please start your truck engine first')
        elif w == 'right':
            if r == 1:
                print('Your truck is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                print('your truck is already moving in right direction')
            else:
                print('please start your truck engine first')
        elif w == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            print('Game over')
            print()
            print()
            break
        else:
            print("invalid command !!")
    while i == 'plane':                                                                     # plane code
        c = input('>')
        if c == 'start':
            if k == 0:
                print('Your plane engine has been started.')
                k,h,q,e = 1,1,1,1
            else:
                print('your plane engine is already started.')
        elif c == 'off':
            if q == 1:
                print('Your plane engine has been turned off.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                print('your plane engine is already off !!')
        elif c == 'forward':
            if k == 1:
                print('Your plane is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                print('your plane is already moving forward')
            else:
                print('please start your plane engine first')
        elif c == 'reverse':
           if h == 1:
                print('Your plane is in reverse gear.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                print('reverse gear is already applied')
           else:
                print('please start your plane engine first')
        elif c == 'left':
            if e == 1:
                print('Your plane is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                print('your plane is already moving in left direction !!')
            else:
                print('please start your plane engine first')
        elif c == 'right':
            if r == 1:
                print('Your plane is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                print('your plane is already moving in right direction')
            else:
                print('please start your plane engine first')
        elif c == 'quit':
            print('Game over')
            k, e, h, q, r, = 0, 0, 0, 0, 0
            print()
            print()
            break
        else:
            print("invalid command !!")
    while i == 'cycle':                                                                               # cycle code
        v = input('>')
        if v == 'start':
            if k == 0:
                print('Your cycle has been unlocked.')
                k,h,q,e = 1,1,1,1
            else:
                print('your cycle is already unlocked.')
        elif v == 'off':
            if q == 1:
                print('Your cycle has been locked.')
                q,k,h,e,r = 0,0,0,0,0
            elif q == 0:
                print('your cycle is already locked !!')
        elif v == 'forward':
            if k == 1:
                print('Your cycle is moving forward.')
                k,e,h,r = 2,1,1,1
            elif k == 2:
                print('your cycle is already moving forward')
            else:
                print('please unlock your cycle first')
        elif v == 'reverse':
           if h == 1:
                print('now your cycle is moving backward.')
                h,k,e,r = 2,1,1,1
           elif h == 2:
                print('your cycle is already moving back')
           else:
                print('please unlock your cycle first')
        elif v == 'left':
            if e == 1:
                print('Your cycle is turning in left direction.')
                e,r,k,h = 2,1,1,1
            elif e == 2:
                print('your cycle is already moving in left direction !!')
            else:
                print('please unlock your cycle first')
        elif v == 'right':
            if r == 1:
                print('Your cycle is turning in right direction.')
                r,e,h,k = 2,1,1,1
            elif r == 2:
                print('your cycle is already moving in right direction')
            else:
                print('please unlock your cycle first')
        elif v == 'quit':
            k, e, h, q, r, = 0, 0, 0, 0, 0
            print('Game over')
            print()
            print()
            break
        else:
            print("invalid command !!")
else:
    print('Wrong password')
