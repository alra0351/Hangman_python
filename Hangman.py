import random
import os

def clear_screen():
    os.system('cls')
    print("Bildschirm geleert")

def main_menu():
    print("(1) Neues Spiel starten")
    print("(2) Statistiken einsehen")
    print("(3) Statistiken löschen")
    print("(4) Beenden")
    user_choice = input()
    if user_choice == "1":
        new_game()
    elif user_choice == "2":
        see_stats()
    elif user_choice == "3":
        del_stats()
    elif user_choice == "4":
        end_game()
    else:
        print("Wrong Input. Choose again")
        main_menu()
        
        
def new_game():
        
    with open("Wortliste.txt", "r") as wordlist:
        lines = wordlist.read().splitlines()
        random_word = random.choice(lines)
    game_string = len(random_word) * "_"
    number_lifes = 5
    while( (random_word != game_string) & (number_lifes > 0) ):
        clear_screen()
        print("Noch %d Leben übrig" % number_lifes)
        print(game_string)
        returns = letter_input(random_word, game_string, number_lifes)
        game_string = returns[0]
        number_lifes = returns[1]        
    if number_lifes > 0:
        clear_screen()
        print("Noch %d Leben übrig" % number_lifes)
        print(game_string)
        print("Du hast das Spiel gewonnen.")
        return 1
    else:
        clear_screen()
        print("Noch %d Leben übrig" % number_lifes)
        print(random_word)
        print("Du hast das Spiel verloren")
        return 0



def game(random_word, game_string, number_lifes):
    while( (random_word != game_string) & (number_lifes > 0) ):
        clear_screen()
        print("Noch %d Leben übrig" % number_lifes)
        print(game_string)
        letter_input(random_word, game_string, number_lifes)
    if number_lifes > 0:
        print("Du hast das Spiel gewonnen.")
    else:
        print("Du hast das Spiel verloren")
        return 0
          
         
def letter_input(random_word, game_string, number_lifes):
    letter = input()
    correct_letters = 0
    word = random_word
    while letter in word:
        letter_pos = word.index(letter)
        list_game_string = list(game_string)
        list_game_string[letter_pos] = letter
        game_string = ""
        for i in list_game_string:
            game_string += i
        list_word = list(word)
        list_word[letter_pos] = " "
        word = ""
        for i in list_word:
            word += i
        correct_letters += 1
    if correct_letters > 0:
        return [game_string, number_lifes]
    else:
        number_lifes -= 1
        return [game_string, number_lifes]
    
    
def see_stats():
    return 0

def del_stats():
    return 0

def end_game():
    return 0

clear_screen()  
main_menu()

# game(x[0], x[1], x[2])


    
    
    






    
    
    