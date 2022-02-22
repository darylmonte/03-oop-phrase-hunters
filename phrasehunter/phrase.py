class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()  # actual phrase the Phrase object is representing


    # prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores
    def display(self, guesses):
        print('')
        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter}', end=' ')
            else:
                print('_', end=' ')
        print('')
        print('')


    # checks to see if the letter selected by the user matches a letter in the phrase
    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False


    # checks to see if the whole phrase has been guessed
    def check_complete(self, guesses):
        for letter in self.phrase:
            if not letter in guesses:
                validate = False
                break
            else:
                validate = True
        return validate
