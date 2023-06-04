import random
import string
import requests


class Hangman:
    def __init__(self) -> None:
        self.WORDLIST_API = 'https://random-word-api.herokuapp.com/word'

    def load_words(self):
        '''
        Returns a list of valid words. Words are strings of lowercase letters.
        '''
        print("Loading word list from file...")
        wordlist = requests.get(self.WORDLIST_API).json()
        print("  ", len(wordlist), "words loaded.")
        return wordlist
    
    def choose_word(self, wordlist):
        '''
        wordlist (list): list of words (strings)
        Returns a word from wordlist at random
        '''
        return random.choice(wordlist)
    
    def is_word_guessed(self, secretWord, lettersGuessed):
        '''
        secretWord (string): the word the user is guessing
        lettersGuessed (list): what letters have been guessed so far
        Returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
        '''
        for letter in secretWord:
            if letter not in lettersGuessed:
                return False
        return True
    
    def get_guessed_word(self, secretWord, lettersGuessed):
        '''
        secretWord (string): the word the user is guessing
        lettersGuessed (list): what letters have been guessed so far
        Returns: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed so far.
        '''
        guessedWord = ''
        for letter in secretWord:
            if letter in lettersGuessed:
                guessedWord += letter
            else:
                guessedWord += '_ '
        return guessedWord
    
    def get_available_letters(self, lettersGuessed):
        '''
        lettersGuessed (list): what letters have been guessed so far
        Returns: string, comprised of letters that represents what letters have not
        yet been guessed.
        '''
        availableLetters = ''
        for letter in string.ascii_lowercase:
            if letter not in lettersGuessed:
                availableLetters += letter
        return availableLetters
    
    def hangman(self, secretWord):
        '''
        secretWord (string): the secret word to guess.
        Starts up an interactive game of Hangman.
        '''
        guessesLeft = 8
        lettersGuessed = []
        print("Welcome to the game, Hangman!")
        print("I am thinking of a word that is", len(secretWord), "letters long.")
        while guessesLeft > 0:
            print("-------------")
            print("You have", guessesLeft, "guesses left.")
            print("Available letters:", self.get_available_letters(lettersGuessed))
            guess = input("Please guess a letter: ")
            guess = guess.lower()
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", self.get_guessed_word(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess)
                if guess in secretWord:
                    print("Good guess:", self.get_guessed_word(secretWord, lettersGuessed))
                    if self.isWordGuessed(secretWord, lettersGuessed):
                        print("-------------")
                        print("Congratulations, you won!")
                        break
                else:
                    print("Oops! That letter is not in my word:", self.get_guessed_word(secretWord, lettersGuessed))
                    guessesLeft -= 1
        if guessesLeft == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", secretWord)

    def main(self):
        wordlist = self.load_words()
        secretWord = self.choose_word(wordlist).lower()
        self.hangman(secretWord)

if __name__ == "__main__":
    hangman = Hangman()
    hangman.main()
