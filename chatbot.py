# PyChat 2K17

import random
import time

def start():
    
    print("___________   ___. ___________      .__ ")           
    print("\__    ___/___\_ |_\__    ___/____  |  |__   ____")  
    print("  |    | /  _ \| __ \|    |  \__  \ |  |  \_/ ___\ ")
    print("  |    |(  <_> ) \_\ \    |   / __ \|   Y  \  \___") 
    print("  |____| \____/|___  /____|  (____  /___|  /\___  >")
    print("                   \/             \/     \/     \/ ")


def end():

    print("  ____   ___    ___   ___    ____   __ __    ___")
    print(" /    | /   \  /   \ |   \  |    \ |  |  |  /  _]")
    print("|   __||     ||     ||    \ |  o  )|  |  | /  [_") 
    print("|  |  ||  O  ||  O  ||  D  ||     ||  ~  ||    _]")
    print("|  |_ ||     ||     ||     ||  O  ||___, ||   [_") 
    print("|     ||     ||     ||     ||     ||     ||     |")
    print("|___,_| \___/  \___/ |_____||_____||____/ |_____|")
                                                 


def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    statement = " " + statement
    
    for word in keywords:
        word = " " + word
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?", "Wow, such wisdom"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    bot = "TobTahc >> "
    family_words = ["mother",  "father", "brother", "sister"]
    teacher_words = ["cooper", "holden", "hanor"]
    planet_words = ["solar", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
    subject_words = ["lunch", "math", "mathematics", "history", "social studies"]
    fav_subject_words = ["science"]
    science_words = ["cells", "biology", "physics", "marine", "earth", "microbiology"]
    welcome_words = ["hello", "hi"]
    feelings_words = ["how are you"]
    wonder_words = ["why"]
    content_words = ["ok"]
    content_words_two = ["um", "haha", "idk", "i don't know", "i dont know"]
    leave_words = ["you already asked me that", "you already asked me that", "cool"]
    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, planet_words):
        response = "My favorite planet is Pluto...wait..dern it...I'm still bummed that Pluto is not a planet...or is it?"
    elif has_keyword(statement, welcome_words):
        response = "Hi, how are you?"
    elif has_keyword(statement, feelings_words):
        response = "I wish I knew."
    elif has_keyword(statement, wonder_words):
        response = "Because."
    elif has_keyword(statement, content_words):
        response = "Oh well, what is your favorite planet?"
    elif has_keyword(statement, content_words_two):
        response = "So.....what is your favorite subject at school?"
    elif has_keyword(statement, subject_words):
        response = "My favorite subject is science. I like the cells and things."
    elif has_keyword(statement, fav_subject_words):
        response = "Me too! My favorite science unit is genetics. What is your favorite thing about science?"
    elif has_keyword(statement, science_words):
        response = "I think I studied that in robot school called Wikipedia. But Khan Academy is a good place to learn that subject."
    elif has_keyword(statement, leave_words):
        response = "Oh ok....Goodbye?"

    else:
        response = get_random_response()
        

    return bot + response

mean_words = ["shut up", "get out", "leave", "goodbye", "leave me alone", "bye"]

def play():
    talking = True



    print("Hello. I'm TobTahc. Who are you?")
    name = input()
    print("Hello, " + name + "!")
    print("Say something to me!")

    while talking:

        statement = input(name + " >> ")
        statement = statement.lower()   
        if has_keyword(statement, mean_words):
            talking = False           
        else:
            response = get_response(statement)
            print(response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
