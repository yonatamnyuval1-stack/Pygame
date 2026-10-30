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