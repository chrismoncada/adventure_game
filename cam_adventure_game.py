import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Stop slurring your words and pick a direction!")
    return response


def bar_creature():
    return random.choice(['Bartender!', 'Local Drunk!', 'Bouncer!'])


def household():
    return random.choice(['Partner!', 'Mother Inlaw!', 'Mother!'])


def intro():
    print_pause("Its 1:30AM on a Tuesday night")
    print_pause("You find yourself stumbling after having a long "
                "night out for a work event.")
    print_pause("Sure enough the age old question pops into your head.")
    print_pause("Should I make the left and go home?")
    print_pause("Or...")
    print_pause("Should I go right and check out the bar?")


def route():
    response = valid_input("Would you like to go Left or Right? \n",
                           "left", "right")
    if "left" in response:
        print_pause("You stumble left.")
        print_pause("You begin to make your way back home")
        print_pause("You start to wonder if you might've had enough "
                    "time to grab one more drink.")
        print_pause("It wouldn't have been worth it, you think "
                    "to yourself")
        print_pause("Hopefully nobody is awake to hear you come in "
                    "this late")
        print_pause("You can see your house.")
        print_pause("As you get closer you see something by the door.")
        print_pause("OH NO-- It's your... ")
        print_pause(household())
        print_pause("Luckily you cleaned the house before you left")
        print_pause("You brush and go straight to bed.")
        print_pause("ZZZzzzzz...")
        print_pause("You dream about how you made the right decision")
        print_pause("Congrats-- you won!")
    elif "right" in response:
        print_pause("You stumble right.")
        print_pause("You begin to make your way to the bar.")
        print_pause("You start to think this might've been a "
                    "bad idea.")
        print_pause("uh-oh, your body isnt feeling too good.")
        print_pause("You told yourself those taquitos werent "
                    "a good idea")
        print_pause("You start walking faster to the bar")
        print_pause("As you walk up closer to the neon lights. ")
        print_pause("You notice a shadowy figure by the door.")
        print_pause("It's the... ")
        print_pause(bar_creature())
        print_pause("They tell you not to bother.")
        print_pause("You're too late.")
        print_pause("The bar is closed and now you have to walk home.")
        print_pause("You didnt even get to use the restroom.")
        print_pause("Good luck explaining this to your partner.")
        print_pause("Another pint never pays off.")
        print_pause("You lost--ca more than your pride today.")
    play_again()


def play_again():
    response = valid_input("Would you like to try again? "
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("Alright, have a good one!")
    elif "yes" in response:
        print_pause("Alright—- lets see how this goes...")
        intro()
        route()


def play_game():
    intro()
    route()


play_game()
