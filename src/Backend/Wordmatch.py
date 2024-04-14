import random

# Function to set the game's difficulty level based on user input
def difficultylevel(category):
    # Loop to handle user input for difficulty level selection
    while True:
        difficulty_choice = input("\nChoose your difficulty\n1: Beginner\n2: Intermediate\n3: Advanced\nAnswer:\t")
        # Format string for building the file path based on category and difficulty
        path = "Python/School/Yahoot/src/Storage/{}/{}"
        # Assign file path and points based on difficulty level chosen
        if difficulty_choice == '1':
            file_path =  path.format(str(category), "Beginner")
            achievable_points = 10
            break
        elif difficulty_choice == '2':
            file_path =  path.format(str(category), "Intermediate")
            achievable_points = 20
            break
        elif difficulty_choice == '3':
            file_path =  path.format(str(category), "Advanced")
            achievable_points = 30
            break
        else:
            print("Invalid option, please enter the corresponding option's number")
    
    words = []

    # Open the file with terms and definitions based on the selected difficulty
    with open(file_path, 'r') as file :
        record = file.readlines()
        for data in record:
            info = data.split()
            words.append(info)
        return words, achievable_points
    

def Game(questions):
    print("\n[---Word Match---]")

    word_output = []
    var = 0
    achievable_points = questions[1]

    # Select a subset of words for the game session
    while len(word_output) < 3:
        data = (questions[0][random.randrange(3)])
        if data not in word_output:
            data[1] = data[1].replace("/", " ")
            word_output.append(data)

    # Display the words and prompt for matching to their definitions
    for resource in word_output:
        var+=1
        print(str(var) + ": " + resource[1])
    print("\nMatch the word to its definition's number!")
    selected_word = word_output[random.randrange(3)][0]

    # Game logic to match words with their definitions
    while True:
        matched_word = input(selected_word + ":\t")
        try:
            if selected_word in word_output[int(matched_word)-1]:
                print("Correct, " + str(achievable_points) + " points awarded\n")
                return True, achievable_points
            else:
                print("Incorrect, The answer is: " + str(selected_word) +"\n") 
                return False
        except ValueError:
           print("Invalid option, please enter the definition's option's number")


def Setup():
    print("\nWelcome to Word Match")

    # Loop to select game category or exit
    while True:
        Category_choice = input("Please Select your category\n1: Art\n2: Computer\n3: History\n4: Math\n5: Return\nAnswer:\t")

        # Handle the game based on the category selected
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
            break  # Exits the loop, thus exiting the setup
        else:
            print("Invalid option, please enter the corresponding option's number\n")
