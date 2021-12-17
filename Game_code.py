import random #this is to import random goodbye


def welcome():
    '''this function will welcome the player ot the game'''
    print('Welcome to "The Impossible Game", named so because only 0.1% of people are able to win...So not impossible, probability speaking, but you get the point! The game is simple, I will ask you one simple question and you will give me one simple answer. Got it? Okay, let us begin.')

def goodbyes(): 
    '''a random goodbye will appear each time the game is over'''
    goodbyes: list[str] = ["Goodbye", "Adios", "I bid you adieu", "Well...see you later"] #list of goodbyes
    goodbye = (goodbyes[random.randint(0,3)])
    actual_name = str(input("What is your name, madame or sire? I'm not kidding. I'm speaking seriously, now. "))
    print(goodbye + " " + actual_name)
    return(goodbye)
def game():
    '''This function will be the game part of the code.  It will ask the question over and over again until the player answers "No".  It will then say bye to the user.'''
    
    print('Welcome to "The Impossible Game", named so because only 0.1% of people are able to win...So not impossible, probability speaking, but you get the point! The game is simple, I will ask you one simple question and you will give me one simple answer. Got it? Okay, let us begin.')
    answer = str(input("What is your name? "))
    if answer == "No" or answer == "no" or answer == "NO" or answer == "N" or answer == "n":
        print("Yay! You won the game! And on the first try! Congratulations! You are officially smarter than 99.9% of the world. Some weirdos actually think their name is What. Pffff.")
        goodbyes()
        print('. Oh, and please invite your friends to take on the impossible challenge that is "The Impossible Game"! See ya! ;)')
#If the player gets the joke the first time, s/he will be praised for their smarts then the game is done after a personalized farewell
    else:
        while not (answer == "No" or answer == "no" or answer == "NO" or answer == "N" or answer == "n"):
            answer = str(input("What is your name? "))
        print("Took you a bit, but yeah! You win! You're smart. Congrats! :D")
        goodbyes()
        print(". And don't forget you can always invite others to this code too. Thank you for your time!")
#When the player gets the joke (after more than one time), s/he will be praised and will get a personalized good-bye

def main ():
    welcome()
    game()
        