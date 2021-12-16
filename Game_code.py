import random #this is to import random goodbye

goodbyes: list[str] = ["Goodbye", "Adios", "I bid you adieu", "Well...see you later"] #list of goodbyes
def game():
    print('Welcome to "The Impossible Game", named so because only 0.1% of people are able to win...So not impossible, probability speaking, but you get the point! The game is simple, I will ask you one simple question and you will give me one simple answer. Got it? Okay, let us begin.')
    answer = str(input("What is your name? "))
    if answer == "No" or answer == "no" or answer == "NO" or answer == "N" or answer == "n":
        print("Yay! You won the game! And on the first try! Congratulations! You are officially smarter than 99.9% of the world. Some weirdos actually think their name is What. Pffff.")
        actual_name = str(input("Okay, all (hilarious) jokes aside. What IS your name? "))
        goodbye = (goodbyes[random.randint(0,3)])
        print( goodbye ", " + actual_name + '. Oh, and please invite your friends to take on the impossible challenge that is "The Impossible Game"! See ya! ;)')

    else:
        while not (answer == "No" or answer == "no" or answer == "NO" or answer == "N" or answer == "n"):
            answer = str(input("What is your name? "))
        print("Took you a bit, but yeah! You win! You're smart. Congrats! :D")
        actual_name = str(input("What is your name, madame or sire? I'm not kidding. I'm speaking seriously, now. "))
        goodbye = (goodbyes[random.randint(0,3)])
        print(goodbye ", "  + actual_name + ". And don't forget you can always invite others to this code too. Thank you for your time!")
        