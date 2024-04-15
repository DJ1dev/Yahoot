import random

# Function to determine the difficulty level based on user input
def difficultylevel(category):
    # Prompt user to choose difficulty level
    difficulty_choice = input("\nChoose your difficulty\n1: Beginner\n2: Intermediate\n3: Advanced\nAnswer:\t")
    # Path format for file retrieval
    path = "Python/School/Yahoot/src/Storage/{}/{}"
    # Determine file path and achievable points based on user's choice
    if difficulty_choice == '1':
        file_path =  path.format(str(category), "Beginner")
        achievable_points = 10
    elif difficulty_choice == '2':
        file_path =  path.format(str(category), "Intermediate")
        achievable_points = 20
    elif difficulty_choice == '3':
        file_path =  path.format(str(category), "Advanced")
        achievable_points = 30
    else:
        print("Invalid option, please enter the corresponding option's number")

    words = []

    # Read words from file and store them in a list
    with open(file_path, 'r') as file :
        record = file.readlines()
        for data in record:
            info = data.split()
            words.append(info[0])
        return words, achievable_points

# Hangman stages represented as Command line art
hanged_man = [
    """
      +-----+
      |   
      |    
      |    
      |
      =========
    """
    ,
    """
      +-----+
      |     O
      |    
      |    
      |
      =========
    """
    ,
    """
      +-----+
      |     O
      |     |
      |    
      |
      =========
    """
    ,
    """
      +-----+
      |     O
      |    /|
      |    
      |
      =========
    """
    ,
    """
      +-----+
      |     O
      |    /|\\
      |    
      |
      =========
    """
    ,
    """
      +-----+
      |     O
      |    /|\\
      |    /
      |
      =========
    """
    ,
    """
      +-----+
      |     O
      |    /|\\
      |    / \\
      |
      =========
    """
]

# Function to start the Hangman game
def Game(words):
    print("[---Hangman---]\nGuess the Word below:")

    achievable_points = words[1]
    word_placeholder =""
    word = ""
    tries = -7

    # Choose a random word from the list
    for character in words[0][random.randrange(len(words))]:
        word_placeholder += '_'
        word += character.lower()
    
    while True:
        # Check if there are still letters to guess and if attempts are remaining
        if '_' in word_placeholder and tries < -1:
            # Display Hangman stage
            print(hanged_man[tries])        
            print(word_placeholder.capitalize())
            # Prompt user to guess a letter
            letter_choice = input("Answer:\t")
            for character in letter_choice.lower():
                # Check if guessed letter is in the word
                if character.lower() in word:
                    # Replace underscore with correct letter
                    word_list = list(word_placeholder)
                    for index, letter in enumerate(word):
                        if letter == character:
                            word_list[index] = character
                    word_placeholder = ''.join(word_list)
                else:
                    tries+=1
        # If attempts are exhausted, end game and display the correct word
        elif tries >= -1:
            print(hanged_man[-1])  
            print("Incorrect, The word was: "+ word.capitalize())
            print("Please Try again")
            return False, False
        else: 
            # If all letters are guessed correctly, congratulate player, display and award points
            print(word.capitalize())
            print("Congrats, you successfully spelt the world\n" + str(achievable_points)+ " points awarded\n")
            return True, achievable_points              
            
 
# Function to set up the Hangman game
def Setup():
    print("\nWelcome to Hangman")

    while True:
        # Prompt user to select a category
        Category_choice = input("Please Select your category\n1: Art\n2: Computer\n3: History\n4: Math\n5: Return\nAnswer:\t")

        # Start game based on user's category choice
        if Category_choice == '1':
            game_results = Game(difficultylevel('Art'))
            #Checks if player won or lost
            if  game_results[0]== True:
                return True, game_results[1]
            else:
                return False
        elif Category_choice == '2':
            game_results = Game(difficultylevel('Computer Science'))
            #Checks if player won or lost
            if game_results[0] == True:
                return True, game_results[1]
            else:
                return False
        elif Category_choice == '3':
            game_results = Game(difficultylevel('History'))
            #Checks if player won or lost
            if game_results[0] == True:
                return True, game_results[1]
            else:
                return False
        elif Category_choice == '4':
            game_results = Game(difficultylevel('Math'))
            #Checks if player won or lost
            if game_results[0] == True:
                return True, game_results[1]
            else:
                return False
        elif Category_choice == '5':
            break
        else:
            print("Invalid option, please enter the corresponding option's number\n")

