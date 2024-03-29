def main():
    c=0
    def hangman():
        import random
        '''
        f = open("t1.txt")
        # need to import text file onto git?
        word_list = f.readlines()
        '''
        word_list=["School", "Pencil", "Toys", "Notebook"]
        choice = random.choice(word_list)
        choice_upper = choice.upper()

        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Ready to play Hangman round", c+1, "?")

        def hangman_display(tries):
            stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
            ]
            return stages[tries]

        underscores = "_" * len(choice_upper)

        print(hangman_display(tries))
        print("_ " * len(choice_upper))
        underscore_change = list(underscores)
        while not guessed and tries > 0:
            guess = input("Enter a letter or a word ")  # user guess
            guess_upper = guess.upper()  # guess in upper to prevent errors

            if len(guess) == 1 and guess_upper.isalpha():  # if letter
                '''
                error handling if guess length is 1 it is a digit 
                or alpha and isalpha checks for simply alpha
                '''

                if guess_upper in guessed_letters:
                    print("you have already guessed this letter")

                elif guess_upper not in choice_upper:
                    tries = tries - 1
                    guessed_letters.append(guess_upper)
                    print('"{}"'.format(guess), "is not in the word")

                else:  # final option- correct guess
                    print("good job", guess_upper, "is in word")
                    guessed_letters.append(guess_upper)


                    placeholder = []
                    index=-1
                    for i in choice_upper:
                        index=index+1
                        if guess_upper == i:
                            placeholder.append(guess_upper)
                        else:
                            placeholder.append(underscore_change[index])

                    underscores = ' '.join(placeholder)
                    print(underscores)
                    underscore_change = placeholder
                    if placeholder  == list(choice_upper) :
                            guessed = True



           ## I have to change this logic , loop will never end otherwise



            elif len(guess) > 1 and guess.isalpha():
                if guess_upper in guessed_words:
                    print("you already guessed that word!")

                elif guess_upper != choice_upper:
                    print(guess, "is not the word")
                    guessed_words.append(guess.upper())
                    tries = tries - 1
                else:
                    guessed = True
                    underscores = choice_upper
                #underscores = ' '.join(placeholder)
                print(" ".join(underscores))
            else:
                tries = tries -1
                print("Not a valid answer")


            if guessed==True:
                print("Congrats you completed round ", c+1)
                print("Well done you won!")
                break
            else:
                print("you have", tries, "tries left")
                print(hangman_display(tries))


        # guess over display where the user is at right now
        if guessed==False:
            print("you lost this round!")

    while c<3:
        hangman()
        c=c+1

main()









