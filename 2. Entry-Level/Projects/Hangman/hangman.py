import json, random, os, subprocess, sys

#############################################################
# ANSI COLOR ESCAPE CODE FUNCTIONS
#############################################################

def red(text):
    text = '\033[31m' + text + '\033[0m'
    return text


def blue(text):
    text = '\033[34m' + text + '\033[0m'
    return text


def green(text):
    text = '\033[32m' + text + '\033[0m'
    return text


def yellow(text):
    text = '\033[33m' + text + '\033[0m'
    return text


def orange(text):
    text = '\033[38;5;214m' + text + '\033[0m'
    return text


def purple(text):
    text = '\033[35m' + text + '\033[0m'
    return text


def pink(text):
    text = '\033[38;5;212m' + text + '\033[0m'
    return text


#############################################################
# HANGMAN FUNCTIONS
#############################################################


def clear_screen():
    clear = ['cls'] if os.name == 'nt' else ['clear'] # Clear terminal screen depending on OS
    subprocess.run(clear, shell=True)


def get_word():
    # Locate base directory whether running as script or PyInstaller bundle
    if hasattr(sys, '_MEIPASS'):
        base_dir = sys._MEIPASS          # bundled .exe temp folder
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # normal script run

    json_path = os.path.join(base_dir, 'words.json')
    with open(json_path, 'r') as f:
        words = json.load(f)

    return words[random.randint(0, len(words) - 1)]


def guess_and_check(ans, correct_let, guesses, wrong_let):
    # Ask user to guess a letter
    letter = input("Enter a letter for your guess: ").lower()
    clear_screen()

    # Check whether or not letter is in answer, if we've already guessed it, or if it's not a letter
    if letter in ans and letter not in correct_let and letter != '':
        print(f"\nThat's a correct letter! There is one or more \'{letter}\' in the answer.\n")
        correct_let.append(letter)
    elif letter in wrong_let or letter in correct_let:
        print(f'\nYou already guessed {letter}. Guess a different letter.\n')
    elif not letter.isalpha() or len(letter) != 1 or letter == '':
        print(f'\n\'{letter}\' isn\'t a letter. Guess a letter.\n')
    else:
        print(f'\nSorry, {letter} is not in the answer.\n')
        wrong_let.append(letter)
        guesses -= 1
    
    match guesses:
        case guesses if guesses > 4:
            print(green(f'REMAINING GUESSES:{guesses}\n'))
        case guesses if guesses > 2:
            print(yellow(f'REMAINING GUESSES:{guesses}\n'))
        case guesses if guesses > 0:
            print(red(f'REMAINING GUESSES:{guesses}\n'))
    return guesses, correct_let, wrong_let


def display_letters(ans, correct_let, wrong_let, rem_guess):
    count = 0
    for letter in ans:
        if letter in correct_let:
            print(f"{letter}", end="") # Print the correct letters for the player to see
            count += 1
        else:
            print("_", end="") # Print underscores to show which letters are still missing
    
    print('\n')
    if count == len(ans):
        print(yellow('CONGRATULATIONS! YOU WIN!\n'))
        input('Press any key to end the game...')
        quit()
    else:
        print(red(f'Incorrect letters: {wrong_let}\n'))
    
    return rem_guess


def main():
    answer = get_word()
    remaining_guesses = 6
    wrong_letters = []
    correct_letters = []
    
    clear_screen()
    print(orange('===HANGMAN===\n'))
    print(green(f'REMAINING GUESSES:{remaining_guesses}\n'))
    while remaining_guesses > 0:
        remaining_guesses = display_letters(answer, correct_letters, wrong_letters, remaining_guesses)
        remaining_guesses, correct_letters, wrong_letters = guess_and_check(answer, correct_letters, remaining_guesses, wrong_letters)
    
    clear_screen()
    input(f'\n{red('===GAME OVER===')}\n\nThe answer was \'{yellow(answer)}\'.\n\n{purple('Press any key to exit...')}')

main()
        