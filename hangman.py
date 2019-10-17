import getpass
#Welcome to... HANGMAN
print("welcome to...")
print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")
#ASCII art for hangman
states = ["""
 _________
 |/      |
 |       |
 |         
 |        
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (_)
 |         
 |        
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (_)
 |       | 
 |       |
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (_)
 |      /| 
 |       |
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (_)
 |      /|\\
 |       |
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (_)
 |      /|\\
 |       |
 |      /  
 |
_|___""",
"""
 _________
 |/      |
 |      (_)
 |      /|\\
 |       |
 |      / \\
 |
_|___"""]

win = False
secret = str(getpass.getpass('Get someone else to give you a word:     '))
def split(word):
    """split string into list"""
    return [char for char in word]

def hangman(secret):
    """Play hangman with word secret"""
    #initial conditions - letters guessed wrong, variables used in computation, splitting the secret into an array (easier to work with)
    a = 0
    i = 5
    wrong_guesses = []
    correct = False
    message = "_ "*len(secret)
    s_list = split(secret)
    current_state = states[a]
    print(current_state)
    print(message)
    while i > 0:
        #guess prompt
        guess = str(input("guess a letter:     "))

        #check if guess is in the secret word
        m_list = split(message)
        for i in range(len(s_list)):
            if s_list[i] == guess:
                m_list.pop(i*2)
                m_list.insert(i*2,guess)
                message = ''.join(m_list)
                correct = True

        #print the next round's stuff
        if correct == False: #If your guess is wrong
            wrong_guesses.append(guess)
            print(f'wrong guesses: {wrong_guesses}')
            a += 1
            i -= 1
            current_state = states[a]
            print(current_state)
            if a == 6:
                return False
            print(message)
        elif '_' in message and correct == True: #If your guess is right, and there are still letters to guess
            print(current_state)
            print(message)
            correct = False
        else: #Win condition - last letter guessed is right, no empty spcaes.
            i = 0
            return True
win = hangman(secret)
if win == True:
    print('You Win!')
else:
    print('You Lose!')