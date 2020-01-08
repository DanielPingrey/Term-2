#Daniel Pingrey
#12/19


import random

questions = ("What is the capital of Serbia? ", "Who is considered to be the leading figure of psychology? ",
            "How many miles wide is Austrailia? ", "Are you glad that you weren't given a crazy question? ",
             "What is Sir Lancelot's favorite color? ", "What region has the Pokemon series made 7 main series games on? ")
             
answers = ("Belgrade", "Sigmund Freud", "2500", "Yes", "Blue", "Kanto")

sep = "================="

status = ""


#opening of the scene
def opening():

    print(sep)
    print("You approach the Bridge of Death and behold the old man from scene 24.")
    print()
    print("As you try to approach the bridge, the old man stops you")
    print()
    print("'Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see'")
    print()
    return


def third_question(status):

    questionIndex = random.randrange(0, len(questions))
    questionAsked = questions[questionIndex]
    answerWanted = answers[questionIndex]

    asked = questionAsked
    asked = input(asked)
    

    if (asked == answerWanted):
        print("\n'Okay you can go'\n")
        status = "You have been arrested by the police for murder and would later die in jail from natural causes"
        print(status)
        return

    
    else:
        status = "'\nYou have been flung into the oblivion and failed your quest for the grail"
        print(status)




opening()
name = input("'What is your name?' ")
quest = input("'What is your quest?' ")
third_question(status)


tombstone = """
        _.---,._,'
       /' _.--.<
         /'     `'
       /' _.---._____
      \\.'   ___, .-'`
           /'    \\\\             .
         /'       `-.          -|-
        |                       |
        |                   .-'~~~`-.
        |                 .'         `.
        |                 |  R  I  P  |
        |                 |   Y O U   |
        |                 |           |
         \\              \\\\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   """

print(tombstone)
print(name)
print("Their quest was", quest)


input()

