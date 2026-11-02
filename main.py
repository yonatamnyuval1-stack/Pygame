def ask(text):
    print(text)
    return input("> ")
def time_travel():
    print("there's an old watch on the sidewalk")
    print("the hands are going backwards, which is wierd")
    choice = ask("1: put it on \n2: leave it")
    if choice == "1":
        put_it_on()
    elif choice == "2":
        leave_it()
    else:
        print("thats not 1 or 2. the watch is still there")
        print("you stand over it until your feet get cold, then you try again")
        time_travel()
def put_it_on():
    print("ok you put it on")
    print("the metal is warm. like someone is just took it off")
    print("everything go quiet for a second")
    print("a bus goes by and the ad on the side is for a phone you never seen")
    print("a newspaper on the ground says 1998")
    street()

def leave_it():
    print("you kick it under a bench and keep walking.")
    print("it start ticking behind you anyway.")
    print("so yeah, leaving it didn't really help.")
    print("it rolls out and bumps your shoe. you pick it up because what else.")
    print("the second it touch your hand the street folds.")
    print("same sidewalk. different cars. the newspaper still says 1998.")
    print("and the kid already saw you kicking it. he looked scared at you.")
    street(saw_you_kick= True)

def street(saw_you_kick=False):
    print("some kid is looking at you like he know you")
    if saw_you_kick:
        print("he stays by the lamp post and doesn't come closer")
    else:
        print("he's maybe ten. red jacket. holding a melted ice cream like he forgot it")
    print("the watch on your wrist jumps a minute back. then another.")
    choice = ask("1: talk to him\n2: read the newspaper\n3: take the watch off ")
    if choice =="1":
        talk_to_kid(saw_you_kick)
    elif choice == "2":
        read_paper()
    elif choice == "3":
        pull_watch()
    else:
        print("you're just stare. the kid stairs back. this is not a plan")
        street(saw_you_kick)

def read_paper():
    print("you pick the paper up. the date is may 14, 1998")
    print("from page is boring, something about a sale and dog that lost")
    print("then on page three there's a little box: man missing since this morning")
    print("no photo. just 'last seen near the bus stop, silver watch' ")
    print("your wrist feels heavier")
    choice = ask("1: go talk to the kid\n2: mess with the crown of the watch")
    if choice =="1":
        talk_to_kid(False)
    elif choice == "2":
        spin_crown()
    else:
        print("the paper blows down the street.")
        street()

def pull_watch():
    print("you try to get it off. the strap isn't even tight")
    print("it just doesn't come. you're fingers slip like the metal is wet")
    print("the kid said quietly, 'he couldn't take it off either'")
    print("so now you kind of have to talk to him")
    talk_to_kid(False)

def spin_crown():
    print("you twist the little crown on the side")
    print("bad idea. the day jumps")
    print("it's night now. same street. rain. the kid is gone now")
    print("a woman is standing where he was, older, holding the same red jacket")
    print("she looks at your wrist and her face goes empty")
    night_street()

def talk_to_kid(saw_you_kick):
    if saw_you_kick:
        print("you say hey. he flinches")
        print("'you kicked uncle's watch' he said. 'that's not funny'")
    else:
        print("you say hey. he does'nt smile but he doesn't run")
        print("'you look like the picture' he says. 'but older and tired'")
    print("his name is Harry(not Potter btw).")
    print("the watch ticks backwards, loud")
    choice = ("1: ask what picture\n2: go with him")
    if chice == "1":
        the_pictue()
    elif choice == "2":
        his_house()
    else:
        print("'you talk weird' he says, and he means the not-answering")
        talk_to_kid(saw_you_kick)

def the_picture():
    print("Harry digs in his pocket and pulls out a bent photo")
    print("it's you. or close. some nose, and younger. the watch is on that wrist now")
    print("'mom's brother' he says. 'he left this morning and the bus never got him'")
    print("you don't remember this morning. you remember your own morning, the real one")
    print("Harry is already walking toward a side street. 'come on. she'll want to see'")
    if choice == "1":
        his_house()
    elif choice == "2":
        spin_crown()
    else:
        print("he waits. he is ten. he can wait longer than you")
        the_picture()
    
def his_house():
    print("the house is small. shoes by the door, a radio talking about the weather")
    print("his mom is at the table with tea")
    print("she looks up and the cup hits the saucer wrong")
    print(" Harry says 'I found him'. she says your name, a name you don't use.")
    print("then she sees the watch and she sits down very slowly")
    choice = ask("1: tell her the truth\n2: say you're just lost\n3: put the watch on the table")
    if choice == "1":
        tell_truth()
    elif choice == "2":
        pretend
    elif choice == "3":
        give_watch
    else:
        print("nobody moves. the radio keeps talking")
        his_house()

def tell_truth():
    print("you tell her you're not from today")
    print("you tell her the sidewalk, the newspaper, the hands going back")
    print("she doesn't laugh")
    print("'he said the same thing' she says. 'before he walked out'")
    print("'if you're him, you're late. if you're not, take that watch of the street'")
    print("Harry is in the doorway, listening to all of it")
    the_choice()

def pretend():
    print("you say you're lost.")
    print("she almost believes you. then the watch skips, out load, in her kitchen")
    print("Harry says 'thats uncle's'. she closes her eyes")
    print("'don't lie in my house' she says. not angry. just done")

def give_watch():
    print("you set it on the table. it slides back to your hand")
    print("no dramatic, just... it won't stay off you")
    print("his mom watches that happen and nods like she expected it")
    print("'then you don't get to drop it and leave' she says")
    print("'he tried. the morning still happened'")
    the_choice()

def the_choice():
    print("the watch is hot now.")
    print("outside, a bus pulls out up at the stop. the door open, nobody gets off")
    print("Harry looks at you like you're the one who decides if today finishes")
    choice = ask("1: get on the bus and go back\n2: stay and walk Harry to school\n3: smash the watch")
    if choice == "1":
        ending_bus()
    elif choice == "2":
        ending_stay()
    elif choice == "3":
        ending_smash()
    else:
        print("the bus door is still open and Harry is still waiting. you picked invalid number and now everyone's have to wait. great, just great")
        the_choice()

def ending_bus():
    print("you apologised to Harry.")
    print("his mom doesn't stop you. she just says 'don't miss it this time'")
    print("you run. the bus smells like wet coats")
    print("the second you sit, the light changes")
    print(" you're one your sidewalk. your sidewalk. cars you know")
    print(" the newspaper in the gutter is today")
    print("but in your pocket there's a bus ticket, may 14, and the seat number is still warm")
    print("for now, the watch is quiet")

def ending_stay():
    print("you say you'll talk to him. his mom hands you a jacket that almost fits")
    print("Harry talks the whole way. a test, friends, normal stuffs")
    print("at the gate he stops")
    print("'if you stay, does he still leave?' he asks")
    print("you don't know. you tell him that, which is the first true easy thing today")
    print("he goes in. the watch stops backwards and just... ticks forward")
    print("you look at the street. you don't know the way home from here")
    print("maybe that's the advanture. maybe you already picked")

def ending_smash():
    print("you hit the watch on the curb. the glass goes into your palm")
    print("Harry is there and also not. you see the read jacket, then a empty doorway")
    print("two versions of the bus stop. one door open. one gone")
    choice = ask("1: step toward 1998\n2: step toward now")

    if choice == "1":
        print("you pick the older street. your hands is still bleeding")
        print("Harry is at the lamp post")
        print("he sees the broken watch and says 'ok, then we do it without it'")
        print("you don't know if thats better. you go with him anyway")
    elif choice == "2":    
        print("you pick your own year. the noise comes back all at once")
        print("on the ground is the bent photo")
        print("the face in it is softer than yours. you put it in your jacket")
    else:
        print("you wait too long. the street picks for you")
        print("you wake up on the bench. both years are gone")
        print("the watch is fixed. the hands are going backwards again")

def night_street():
    print("the woman says 'I told him not to wear it out of the house'")
    print("she thinks you're him. the older one.")
    print("rain in your collar. the watch is cold this time, not hot")
    choice = ask("1: ask where Harry\n2: ask how to get back to the morning")
    if choice == "1":
        print("'school' she says. 'he's ten. he's always at school in this one'")
        print("she looks tired in a way that took years.")
        print("'if you can still find the morning, go. i already lived this night'")
        print("you twist the crown the other way before you can think about it")
        print("you get another try. don't waste the morning")
        street()
    elif choice == "2":
        print("she points at your wrist. 'back. always back. it only goes one way until you mean it'")
        ending_bus()
    else:
        print("she waits in the rain like she's done it to you before")
        night_street()

def main():
    print("Hello! you going to your adventure!")
    print("Please choose your adventure number!")
    print("1: Time travel")
    print("2: Explore the ocean")
    print("3: servive on mars")
    choose1 = input("> ")
    if choose1 == "1":
        time_travel()
    elif choose1 == "2":
        ocean()
    elif choose1 == "3":
        mars()
    else:
        print("invalid choose")
main()