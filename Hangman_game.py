
import random
import os

MSG = """   
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║    HHH   HHHH       AAAA       NNNNN     NNN    hhhhhhh      MMM       MMM       AAAA       NNNNN    NNN    ╔═══════╗        ║
║    HHH   HHHH      AAAAAA      NNNNNN    NNN   hhhhhhhh      MMMMM   MMMMM      AAAAAA      NNNNNN   NNN    ║     (o_0)      ║
║    HHHHHHHHHH     AAA  AAA     NNN NNN   NNN  hhh            MMM MM MM MMM     AAA  AAA     NNN NNN  NNN    ║      _|_       ║
║    HHHHHHHHHH    AAAAAAAAAA    NNN  NNN  NNN  hhh   hhhhhhh  MMM   M   MMM    AAAAAAAAAA    NNN  NNN NNN    ║       |        ║
║    HHH    HHH   AAA      AAA   NNN   NNNNNNN   hhhhhhh  hhh  MMM       MMM   AAA      AAA   NNN   NNNNNN    ║       |        ║
║    HHH    HHH  AAA        AAA  NNN    NNNNNN     GGGGG  GGG  MMM       MMM  AAA        AAA  NNN    NNNNN    ║       /\       ║
║                                                                                                                              ║
║                                                Welcome to the Hangman game                                                   ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

"""

GAME_OVER = """
          GGGGGGGG          AAAA       MMM      MMM  EEEEEEEEE        OOOO     VVV         VVV  EEEEEEEEE  RRRRRRR
         GGGGGGGGG         AAAAAA      MMMMM   MMMM  EEEEEEEEE     OOO    OOO   VVV       VVV   EEEEEEEEE  RRRRRRRRR
        GGG               AAA  AAA     MMM MM M MMM  EEE          OOO      OOO   VVV     VVV    EEE        RRR   RRRR
        GGG   GGGGGGG    AAAAAAAAAA    MMM   M  MMM  EEEEEE       OOO      OOO    VVV   VVV     EEEEEE     RRRRRRRRR
         GGGGGGG  GGG   AAA      AAA   MMM      MMM  EEE           OOO    OOO      VVV VVV      EEE        RRR  RRR
          GGGGGG  GGG  AAA        AAA  MMM      MMM  EEEEEEEEE        OOOO           VVV        EEEEEEEEE  RRR   RRRR

"""


def read_words ():
    words = []
    with open("./archivos/data.txt","r", encoding="utf-8") as f:
        for word in f:
            words.append(word)
    #select the ramdom word
    random_word = random.choice(words)
    return random_word

    
def run():
    cont_letters = 0
    cont_try = 0
    status = True
    os.system("cls")
    print(MSG)

    letter_list = []
    word_hang = read_words()
    word_hang = word_hang.strip()
    num_letters = len(word_hang)
    under_list = ["_"] * num_letters
    letter_list = [letter for letter in word_hang]
    
    while status:
        status_insert = False
        os.system("cls")
        print(MSG)
        #print(letter_list)
        print('Guess the word!')
        print('')
        for element in under_list:
            print(element + " ", end="")
        print("\n")
        
        letter_in = input('Enter any letter: ')
        letter_in = letter_in.lower()
        try:
            if letter_in == '' or letter_in.isalpha() == False or len(letter_in) != 1 :
                raise ValueError("Only enter a letter!")
            for index, letter in enumerate(letter_list):
                if letter == letter_in:
                    status_insert = True 
                    index_aux = index
                    letter_aux = letter    
        except ValueError as ve:
            print(ve)
            os.system("pause")
            continue
        
        if status_insert == True:
            cont_letters = cont_letters + 1
            under_list[index_aux] = letter_aux
            letter_list[index_aux] = "*"
        else:
            cont_try = cont_try + 1
        
        if cont_letters == num_letters:
            os.system("cls")
            print(MSG)
            print('Congratulations you won!!')
            print('The word was: ' + word_hang )

            break
        if cont_try >= num_letters:
            os.system("cls")
            print(GAME_OVER)
            print('                                               The word was: ' + word_hang )
            break

        
if __name__ == "__main__":
    run()