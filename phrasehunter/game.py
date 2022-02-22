from phrasehunter.phrase import Phrase
import random
import os


class Game:

    def __init__(self):
        self.missed = 5  # used to track the number of incorrect guesses by the user
        self.phrases = self.create_phrase()  # list of quotes
        self.active_phrase = self.get_random_phrase()  # Phrase object that's currently in play
        self.guesses = [' ',"'",'!',',']  # This is a list that contains the letters guessed by the user


    def create_phrase(self):
        quotes = [
            "There's no place like home",
            "I'm the king of the world!",
            "I'll be back",
            'Houston, we have a problem',
            'My precious',
            'Just keep swimming',
            'It was beauty killed the beast',
            'Snap out of it!',
            'You had me at hello',
            'To infinity and beyond'
        ]
        phrases = []
        for quote in quotes:
            phrases.append(Phrase(quote))
        return phrases


    def start(self, user_guess):
        self.welcome()  # calls the welcome method
        while self.missed > 0 and not self.active_phrase.check_complete(self.guesses):
            print('~' * 22)
            print(f' # of tries left : {self.missed}')
            print('~' * 22)
            
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()  # calls the get_guess method
            self.guesses.append(user_guess)  # adds the user's guess to guesses
            
            # https://docs.python.org/3/library/stdtypes.html#str.isalpha
            if not user_guess.isalpha():  # checks if guess is or doesn't have a number
                print('Letters only. Please try again.')
            elif len(user_guess) > 1:
                print('Please enter one letter at a time. Try again.')
            elif not self.active_phrase.check_guess(user_guess):
                self.missed -= 1  # decrements the number of missed by one if the guess is incorrect
            os.system('clear')
        self.game_over()  # calls the game_over method

    # randomly retrieves one of the phrases stored in the phrases list
    def get_random_phrase(self):
        return random.choice(self.phrases)


    def welcome(self):
        print('')
        print('=' * 25)
        print(' Guess that Movie Quote ')
        print('=' * 25)
        print('')

    # gets the guess from a user and records it in the guesses attribute
    def get_guess(self):
        guess = input('Enter a letter: ')
        return guess.lower()

    # asks if player wants to play again after a round
    def play_again(self):
        choice = input('Would you like to play again? [y]es or [n]o: ')
        if choice.lower() != 'y' and choice.lower() != 'n':
            print('\nThat is not a valid response. Have a good day!\n')
            exit()
        elif choice.lower() == 'n':
            print('\nThank you playing. Have a good day!\n')
            exit()
        elif choice.lower() == 'y':
            self.missed = 5
            self.active_phrase = self.get_random_phrase()
            self.guesses = [' ',"'",'!',',']
            os.system('clear')
            self.start(self.get_guess)


    # displays a friendly win or loss message and asks if user wants to play again
    def game_over(self):
        if self.missed == 0:
            print('\nSorry, you lost. The game is over.\n')
        else:
            print(f'\n“{self.active_phrase.phrase}”\n')
            print('Congratulations! You won!\n')
        self.play_again()