art_list=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
           )
           
word_list=["mouse","chase","killer","maniac","evil"]

current_word=random.choice(word_list)

blanks_string=["-"]*len(current_word)

blanks=len(current_word)
lives=6
print(blanks_string)


while(blanks>0 and lives>0):
    
    enterd_letter=input(f"Enter a letter({lives}/6 lives): ")
    
    if enterd_letter in current_word:
        blanks-=1
        i=0
        index=current_word.index(enterd_letter)
        current_word=current_word.replace(enterd_letter,'\0',1)
        blanks_string[index]=enterd_letter
        
        
        print(blanks_string)
        
        if blanks==0:
            break
        
    else:
        
        print(blanks_string)
        print(art_list[lives-1])
        lives-=1
        if lives==0:
            break
        
        
        
        
        