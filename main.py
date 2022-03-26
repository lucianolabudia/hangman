import random
import hangman_words
import hangman_art
import os


def main():

    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6

    print(hangman_art.logo)
    print("\n")
    
    # Testing code
    #print(f'La solucion es {chosen_word}')

    display = []    
    for _ in range(word_length):
        display += "_"
    print(display)

    

    while not end_of_game:

        guess = input("Adivina una letra: ").lower()

        os.cls()

        if guess in display:
            print(f"Ya has adivinado la letra {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Posición actual: {position}\n Letra actual: {letter}\n Letra supuesta: {guess}")
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"Elegiste la letra: {guess}, que no está en la palabra. Pierdes una vida.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("Perdiste =(")

        
        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("GANASTE!!!")

        print(hangman_art.stages[lives])




# ============================
if __name__ == '__main__':
    main()