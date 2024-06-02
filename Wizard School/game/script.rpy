# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

python:
    house = ""


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "This is the beginning of the game."

    "You arrive at the school."

    jump sorting

label sorting:
    "The school is very large."

    "A man approaches you with a hat."

    show secretary at top

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip().capitalize()

    if player_name == "":
        $ player_name = "Joe"

    e "Nice to meet you, [player_name]!"

    e "This is our tradition. Answer the hat truthfully or misfortune will befall you."

    "You hear a voice in your head asking a question."

    menu:

        "If you were an animal you would be a..."

        "Great Owl":

            jump join_strix

        "Rattus":

            jump join_merlot

        "Bog Salamander":

            jump join_golgotha

        "Unicorn":

            jump join_unicorn

label join_strix:
    e "Welcome to Strix house!"

    $ house = "strix"

    jump dorm

label join_merlot:
    e "Welcome to Merlot house!"

    $ house = "merlot"

    jump dorm

label join_golgotha:
    e "Welcome to Golgotha house!"

    $ house = "golgotha"

    jump dorm

label join_unicorn:
    e "Welcome to Unicorn house!"

    $ house = "unicorn"

    jump dorm

label dorm:
    e "Lets get you to your dorm!"

    e "You'll love the [house] dorm."

    jump meet_friend

label meet_friend:
    e "This is your new friend, Jimbo."

    e "Alright its time for bed."

    python:

        is_first_day = True
        date = 1
        day = 0
        days_of_week = {
            0: 'Sunday',
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday'
        }

    jump new_day

# This is the beginning of each new day.
label new_day:
    if is_first_day:
        
        $ is_first_day = False

        "Its your first day at Haven academy."

        "You need to get decide on your schedule today, better head down to the front office."

        

    else:
        "Just another day in the life."

    "You roll over and check your calendar."

    "It says today is [date], a [days_of_week[day]]."

    "Welp time for bed again"

    $ date += 1
    $ day = (day + 1) % 7

    jump new_day