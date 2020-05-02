import random
import string

Word_list_filename = "eff_large_wordlist.txt"

def load_wordlist():
    print("Loading wordlist...")
    input_File = open(Word_list_filename, 'r')
    content = input_File.readlines()
    random_line = random.choice(content)
    input_File.close()
    
    return random_line


ran_word = load_wordlist()
ran_word = ''.join(filter(str.isalpha, ran_word))

letter = ''
gamevar = 1
masked_word = []
letter_list = []
askstatus = 0

print("H A N G M A N")
print("Guess the right word.")
print("You have 8 missmatches until you are hanged!")

while gamevar == 1:
    askstatus = 0
    while askstatus == 0:
        gamestat = input("Type \"play\" to play the game, \"exit\" to quit: ")
        if gamestat == 'play':
            gamevar = 1
            askstatus += 1
        elif gamestat == 'exit':
            askstatus += 2
        else:
            askstatus = 0

    if askstatus == 2:
        break

    counter = 9
    letter_list.clear()
    masked_word.clear()

    for i in range(len(ran_word)):
        masked_word.append('-')

    while counter > 1:

        print('')
        print(''.join(masked_word))
        letter = input("Input a letter: ")

        if not letter.isalpha() or letter.isupper():
            print("It is not an ASCII lowercase letter")
        elif letter not in ran_word and letter not in letter_list and len(letter) == 1:
            print("No such letter in the word")
            counter -= 1
        if len(letter) != 1:
            print("You should print a single letter")
        if letter in letter_list:
            print("You already typed this letter")

        letter_list.append(letter)

        for i in range(len(ran_word)):
            if ran_word[i] == letter:
                masked_word[i] = letter

        if ''.join(masked_word) == ran_word:
            print("You guessed the word!")
            print("You survived!")
            counter = 0
            print('')

        if counter == 1:
            print("You are hanged!")
            print("The word was: {}".format(ran_word))
            print('')
