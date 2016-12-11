# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 21:33:43 2016
Hangman game
@author: r4ndomw4lk
"""

class Hangman:
    
    words_list=['soldier', 'computer','cohort','work', 
    'horse', 'house', 'dragon', 'doll','boss', 'bomb',
    'bastion','plane','bull','heart','liver','lion',
    'laser','lord','rope','ring','rat']
    
    def __init__(self):
        
        print('Hello to the hangman game')
        word=self.word_selection()
        hidden_word=self.hide_word(word)
        print('Here is your word to guess: ' + hidden_word)
        print('You have 5 turns to guess a word. Good luck!')
        n=0
        guessed_letters=[]
        while n<5:
            print('Turn '+str(n))
            letter=self.get_letter()
            guessed_letters.append(letter)
            if self.check_if_letter_in_word(letter, word):
                print('Good')
                print(self.reveal_letter(letter, word, guessed_letters))
            else:
                print('The letter is not in word.')
            n+=1
        
    def word_selection(self):
        import random
        return(self.words_list[random.randint(0,len(self.words_list)-1)])
        
    def hide_word(self, word):
        word_hidden=''
        for i in range(0, len(word)):
            word_hidden+='*'
        return(word_hidden)
        
    def get_letter(self):
        import string
        letter=input('Please name a letter: ')
        if len(letter)>1 or letter.lower() not in string.ascii_lowercase:
            print('Wrong letter. Please try again.')
            self.get_letter()
        else:
            return(letter)
            
    def check_if_letter_in_word(self,letter,word):
        if letter in word:
            return True
        else:
            return False
    
    def reveal_letter(self, letter, word, guessed_letters):
        new_hidden_word=''
        for w in word:
            if w not in guessed_letters:
                new_hidden_word+='*'
            else:
                new_hidden_word+=w
        return(new_hidden_word)
            
        
