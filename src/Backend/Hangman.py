import random


def difficultylevel(category):
    difficulty_choice = input("\nChoose your difficulty\n1: Beginner\n2: Intermediate\n3: Advanced\nAnswer:\t")
    path = "Python/School/Yahoot/src/Storage/{}/{}"
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

    with open(file_path, 'r') as file :
        record = file.readlines()
        for data in record:
            info = data.split()
            words.append(info[0])
        return words, achievable_points

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
    "      +-----+\n      |     O\n      |    /|\ \n      |   \n      | \n      ========="
    ,
    "      +-----+\n      |     O\n      |    /|\ \n      |    /\n      | \n      ========="
    ,
    "      +-----+\n      |     O\n      |    /|\ \n      |    / \ \n      | \n      ========="
]

def Game(words):
    print(words)
    print("[---Hangman---]\nGuess the Word below:")

    achievable_points = words[1]
    word_placeholder =""
    word = ""
    tries = -7

    for character in words[0][random.randrange(len(words))]:
        word_placeholder += '_'
        word += character.lower()
    print(word.capitalize())
    while True:
        if '_' in word_placeholder and tries < -1:
            print(hanged_man[tries])        
            print(word_placeholder.capitalize())
            letter_choice = input("Answer:\t")
            for character in letter_choice.lower():
                if character.lower() in word:
                    word_list = list(word_placeholder)
                    for index, letter in enumerate(word):
                        if letter == character:
                            word_list[index] = character
                    word_placeholder = ''.join(word_list)
                else:
                    tries+=1
        elif tries >= -1:
            print("You Failed, The word was: "+ word.capitalize())
            print("Please Try again")
            return False
        else: 
            print(word.capitalize())
            print("Congrats, you successfully spelt the world\n" + str(achievable_points)+ " points awarded\n")
            return True, achievable_points
            
 
def Setup():
    print("\nWelcome to Hangman")

    while True:
        Category_choice = input("Please Select your category\n1: Art\n2: Computer\n3: History\n4: Math\n5: Return\nAnswer:\t")

        if Category_choice == '1':
            game_results = Game(difficultylevel('Art'))
            if  game_results[0]== True:
                return True, game_results[1]
            else:
                return False
        elif Category_choice == '2':
            game_results = Game(difficultylevel('Computer Science'))
            if game_results[0] == True:
                return True, game_results[1]
            else:
                return False
        elif Category_choice == '3':
            game_results = Game(difficultylevel('History'))
            if game_results[0] == True:
                return True, game_results[1]
            else:
                return False
        elif Category_choice == '4':
            game_results = Game(difficultylevel('Math'))
            if game_results[0] == True:
                return True, game_results[1]
            else:
                return False
        elif Category_choice == '5':
            break
        else:
            print("Invalid option, please enter the corresponding option's number\n")