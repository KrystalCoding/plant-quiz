import random
import textwrap
import sys
import os

# The list of questions and answers in the quiz game
questions = [
    {
        "question":
        "What is the scientific name for the common sunflower?",
        "answers":
        ["Rosa rubiginosa", "Cucurbita pepo", "Helianthus annuus",
         "Lilium auratum"],
        "correct_answer": "Helianthus annuus"
    },
    {
        "question":
        "What is the most widely cultivated fruit in the world?",
        "answers":
        ["Apple", "Banana", "Mango", "Orange"],
        "correct_answer": "Banana"
    },
    {
        "question":
        "What type of plant is poison ivy?",
        "answers":
        ["Vine", "Shrub", "Tree", "Grass"],
        "correct_answer": "Vine"
    },
    {
        "question":
        ("What is the process called by which plants convert light"
         " into energy?"),
        "answers":
        ["Respiration", "Transpiration", "Fertilization", "Photosynthesis"],
        "correct_answer": "Photosynthesis"
    },
    {
        "question":
        "What is the largest flower in the world?",
        "answers":
        ["Titan arum", "Corpse flower", "Rafflesia arnoldii",
         "Hydrangea macrophylla"],
        "correct_answer": "Rafflesia arnoldii"
    },
    {
        "question":
        "What is the most common element found in all living organisms?",
        "answers":
        ["Oxygen", "Carbon", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon"
    },
    {
        "question":
        "What is the name of the largest tree in the world?",
        "answers":
        ["Sequoia sempervirens", "Eucalyptus regnans", "Picea sitchensis",
         "Sequoiadendron giganteum"],
        "correct_answer": "Sequoiadendron giganteum"
    },
    {
        "question":
        ("What is the process called by which plants"
         " lose water through their leaves?"),
        "answers":
        ["Transpiration", "Photosynthesis", "Respiration", "Fertilization"],
        "correct_answer": "Transpiration"
    },
    {
        "question":
        "What is the national flower of Japan?",
        "answers":
        ["Lotus", "Rose", "Cherry blossom", "Tulip"],
        "correct_answer": "Cherry blossom"
    },
    {
        "question":
        ("What is the name of the plant tissue that transports water"
         " and nutrients from the roots to the rest of the plant?"),
        "answers":
        ["Phloem", "Xylem", "Cambium", "Epidermis"],
        "correct_answer": "Xylem"
    },
    {
        "question":
        ("What is the name of the process by which plants"
         " bend or grow towards a light source?"),
        "answers":
        ["Gravitropism", "Hydrotropism", "Thigmotropism", "Phototropism"],
        "correct_answer": "Phototropism"
    },
    {
        "question":
        "What is the name of the process by which plants shed their leaves?",
        "answers":
        ["Transpiration", "Abcission", "Photosynthesis", "Respiration"],
        "correct_answer": "Abcission"
    },
    {
        "question":
        ("What is the name of the chemical compound responsible for"
         " giving plants their green color?"),
        "answers":
        ["Chlorophyll", "Carotenoid", "Anthocyanin", "Chloroform"],
        "correct_answer": "Chlorophyll"
    }
]


def clear_screen():
    """
    Clears the screen based on the user's operating system.
    """
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def player_info():
    """
    Prompts the user to enter their preferred username
    and returns it as a string.
    """
    while True:
        player_name = input("Please enter your preferred username: ")
        if player_name:
            break
        print("Username can not be empty, please try again.")
    # Print a blank line for formatting
    print()
    welcome(player_name)
    return player_name


def welcome(player_name):
    """
    Prints a welcome message to the user.
    """
    print(f"Hello, {player_name}! Welcome to the Plant Quiz.\n")
    print("Press Enter to test your plant knowledge with"
          " 13 questions:\n")
    input()


def run_game():
    """
    Runs the Plant Quiz game.
    This function shuffles the questions, initializes the score,
    asks the user to answer each question, and updates the
    score based on the user's answers. After all questions are answered,
    the user's score is displayed.
    """
    # Shuffle the questions
    random.shuffle(questions)
    # Initialize the score
    score = 0
    # Clear the screen at the start of each round
    clear_screen()
    for i, question in enumerate(questions):
        # Wrap the question text to a maximum width of 80 characters
        wrapped_question = textwrap.wrap(question['question'], width=80)
        # Print each line of the wrapped question
        for line in wrapped_question:
            print(line)
        for j, answer in enumerate(question['answers']):
            # Wrap each answer text to a maximum width of 80 characters
            wrapped_answer = textwrap.wrap(answer, width=80)
            # Print each line of the wrapped answer
            for line in wrapped_answer:
                print(f"{j + 1}. {line}")
        while True:
            player_answer = input("Enter your answer (1-4): ")
            if player_answer.isdigit() and int(player_answer) in [1, 2, 3, 4]:
                break
            print("Invalid input. Please enter a number between 1 and 4.")
        if player_answer == str(question['answers'].index
                                (question['correct_answer'])+1):
            print("Correct!")
            score += 1
        else:
            print("Incorrect."
                  f" The correct answer is {question['correct_answer']}.")
        # Print a blank line for formatting
        print()
        if score == 13:
            print(f"Congratulations, {player_name}! You are a plant Master!")
    print(f"Game over. Your score is {score}/{len(questions)}.")
    # Print a blank line for formatting
    print()
    # Ask the user if they want to play again.
    while True:
        play_again = input("Try again? (y/n): ")
        if play_again.lower() == "y":
            run_game()
        elif play_again.lower() == "n":
            print("Thanks for playing!")
            sys.exit()
        print("Invalid input. Please enter 'y' or 'n'.")


# Get player name
player_name = player_info()

# Run the game
run_game()
