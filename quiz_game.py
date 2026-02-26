# quiz_game.py - Python Quiz Game
# Starter code for e004-exercise-control-flow (Collaborative Project)
import random
import os

"""
Python Quiz Game
----------------
A multiple-choice quiz game that tests Python knowledge.

This is a collaborative project - use pair programming!
- Driver: Types the code
- Navigator: Reviews and guides

Switch roles every 20-30 minutes!
"""

# =============================================================================
# TODO: Task 1 - Question Bank (Driver 1)
# =============================================================================

def create_question_bank():
    """
    Return a list of quiz questions.
    
    Each question is a dictionary with:
    - question: The question text
    - options: List of 4 options (A, B, C, D)
    - answer: Correct answer letter
    - explanation: Why this answer is correct
    
    Add at least 10 questions covering Week 1 topics.
    """
    questions = [
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A) func", "B) def", "C) function", "D) define"],
            "answer": "B",
            "explanation": "The 'def' keyword is used to define functions in Python.",
            'category' : "Python Syntax"
        },
        # TODO: Add 9 more questions covering:
        # - Python syntax and indentation
        # - Data types (strings, lists, dictionaries)
        # - Control flow (if/else, loops)
        # - Functions and parameters
        # - Variables and operators

        {
            "question": "How many tabs are needed after writing the function name if there's 4 spaces in a tab",
            "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
            "answer": "A",
            "explanation": "Python requires 1 tab",
            'category': "Python Syntax"
        },

        {
            "question": "What is a string in python",
            "options": ["A) float number", "B) objects that contains character(s) ", "C) algorithm", "D) whole number"],
            "answer": "B",
            "explanation": "Strings are a sequence of characters in python",
            'category': "Python Syntax"
        },

        {
            "question": "How do you find the type of an object?",
            "options": ["A) which(object)", "B) print(object)", "C) object.type()", "D) use type(object)"],
            "answer": "D",
            "explanation": "the type() function will return the type of the object passed inside",
            "category": "Other"
        },

        {
            "question": "What keyword do you use to initialize a variable in python?",
            "options": ["A) The type of the variable", "B) No keyword", "C) var", "D) let"],
            "answer": "B",
            "explanation": "There is no keyword required because python variable are dynamically typed.",
            "category": "Variables and Operators"
        },

        {
            "question": "What is \"10\" + \"23\" in Python?",
            "options": ["A) error", "B) undefined", "C) 1023", "D) 23"],
            "answer": "C",
            "explanation": "Since both data types are string, they will concatenated instead of added like numbers",
            "category": "Variables and Operators"
        },

        {
            "question": "how do you find the occurences of a character ch in a string S in base Python?",
            "options": ["A) s.findAll(ch) ", "B) s.count(ch)", "C) s.find(ch)", "D) s.charAt(ch)"],
            "answer": "B",
            "explanation": "The count function finds the number of occurences.",
            "category": "Other"
        },

        {
            "question": "Which symbol is the greater than sign?",
            "options": ["A) ==", "B) <", "C) >", "D) ++"],
            "answer": "C",
            "explanation": "> represents the greater than in Python",
            "category": "Variables and Operators"
        },
        {
            "question": "How to write a single line comment in Python?",
            "options": ["A) !--", "B) //", "C) !-", "D) #"],
            "answer": "D",
            "explanation": "# is the Python way to write a single comment, the others are from other languages",
            "category": "Python Syntax"
        },
        {
            "question": "What is the correct syntax for a do while loop in Python",
            "options": ["A) do: (..) while (..)", "B) do {} while(..)", "C) while(..) do {}", "D) do: for(..)"],
            "answer": "B",
            "explanation": "The do comes first, enclosed in curly braces, then use the while loop",
            "category": "Control Flow"
        }
    ]
    return questions


# =============================================================================
# TODO: Task 2 - Core Game Functions (Driver 2)
# =============================================================================

def display_question(question, number, total): # use multi-line string to format the string
    """
    Display a question and its options.
    
    Args:
        question: A question dictionary
        number: The current question number (1-based)
        total: Total number of questions
    
    Output format:
    --------------------------------------------------
    Question 1 of 10
    --------------------------------------------------
    [question text]
    
    A) option A
    B) option B
    C) option C
    D) option D
    """
    # TODO: Implement this function
    question_text = f'''
    --------------------------------------------------
    Question {number} of {total}
    --------------------------------------------------
    {question['question']}
    
    {question["options"][0]}
    {question["options"][1]}
    {question["options"][2]}
    {question["options"][3]}

'''
    print(question_text)


def get_user_answer():
    """
    Get and validate user input.
    
    Keep prompting until the user enters a valid answer (A, B, C, or D).
    Accept both uppercase and lowercase input.
    
    Returns:
        A valid answer in uppercase (A, B, C, or D)
    """
    # TODO: Implement input validation loop
    while (True):
        user_input = input("Enter your answer here >")
        if not user_input.upper() in ["A","B","C","D"]: # check to make sure its valid
            print("invalid input, try again")
        else: # returns the user input as upper case letter
            return user_input.upper()


def check_answer(question, user_answer):
    """
    Check if the user's answer is correct.
    
    Args:
        question: The question dictionary
        user_answer: The user's answer (uppercase letter)
    
    Returns:
        True if correct, False otherwise
    """
    # TODO: Compare user_answer with question["answer"]
    return (question["answer"].upper() == user_answer) # compare answer to user answer


def display_feedback(question, user_answer, is_correct):
    """
    Display feedback after answering a question.
    
    If correct: Print "Correct!" with green styling (or just text)
    If incorrect: Print "Incorrect. The answer was X."
    Always show the explanation.
    """
    # TODO: Display appropriate feedback based on is_correct
    if is_correct: # if answer is correct, then give them the green
        print("\033[92mCorrect ✅\033[0m")
    else: # incorrect answer given
        answer = question["answer"]
        print(f"\033[91mIncorrect ❌ The answer was {answer}\033[0m")
    print(f"Reason:{question["explanation"]}")

# =============================================================================
# TODO: Task 3 - Game Loop (Driver 1)
# =============================================================================

def run_quiz(questions):
    """
    Run the complete quiz game.
    
    1. Display welcome message
    2. Loop through all questions
    3. For each question:
       - Display the question
       - Get user answer
       - Check if correct
       - Display feedback
       - Update score
    4. Return final score
    
    Args:
        questions: List of question dictionaries
    
    Returns:
        Tuple of (score, total_questions)
    """
    score = 0
    total = len(questions)

    categories = {
        1: "Python Syntax",
        2: "Data Types",
        3: "Control Flow",
        4: "Functions and Parameters",
        5: "Variables and Operators",
        6: "Other",
        7: "All"
    }
    
    # Welcome message
    print("=" * 50)
    print("     WELCOME TO THE PYTHON QUIZ GAME!")
    print("=" * 50)
    print(f"\nYou will answer {total} questions.")
    print("Enter A, B, C, or D for each question.\n")
    input("Press Enter to start...")
    category_choice = -1
    try:
        category_choice = int(input("""
        Select a category to practice:
        1. Python Syntax
        2. Data Types
        3. Control Flow
        4. Functions and Parameters
        5. Variables and Operators
        6. Other
        7. All
    """))
    except Exception:
        print("Error")
        exit(-1)
    
    if(category_choice <= 0 and category_choice >= 8):
        print("Invalid selection, practicing all questions")
        exit(-1)
        
    
    # TODO: Implement the game loop
    # Hint: Use a for loop with enumerate
    random.shuffle(questions)
    for i, question in enumerate(questions):
        if(question['category'] != categories[category_choice]):
            continue
        display_question(question, i, len(questions)) # display question
        ans = get_user_answer() # get answer from user
        correct = check_answer(question, ans) # validation
        display_feedback(question, ans, correct) # show feedback
        if correct: # counter for score
            score += 1
        input("press enter to move on to the next question...") # stop the user from clearing the screen instantly after answering question
        os.system('cls' if os.name == 'nt' else 'clear') # logic to clear screen for all systems

    return score, total


# =============================================================================
# TODO: Task 4 - Results and Grading (Driver 2)
# =============================================================================

def calculate_grade(score, total):
    """
    Calculate letter grade based on percentage.
    
    Grading scale:
    - 90-100%: A
    - 80-89%:  B
    - 70-79%:  C
    - 60-69%:  D
    - Below 60%: F
    
    Args:
        score: Number of correct answers
        total: Total number of questions
    
    Returns:
        Letter grade as string
    """
    # TODO: Calculate percentage and return grade
    percent = (float(score) / total) * 100
    if(percent >= 90):
        return 'A'
    elif(percent >= 80):
        return 'B'
    elif(percent >= 70):
        return 'C'
    elif(percent >= 60):
        return 'D'
    return 'F'


def display_results(score, total):
    """
    Display final results with grade and encouragement.
    
    Include:
    - Score (e.g., 8/10)
    - Percentage
    - Letter grade
    - Encouraging message based on performance
    """
    # TODO: Calculate percentage and grade
    grade = calculate_grade(score, total)
    percent = (float(score) / total) * 100
    # TODO: Display formatted results
    # TODO: Add encouragement message
    encouraging_message = ""
    if(grade == 'A'):
        encouraging_message = "Keep it up, you're doing well!"
    else:
        encouraging_message = "Had a good try! Hope you don't have to see this."
    print(f"""
    Score: {score} / {total}
    Percentage: {percent:.1f}
    Letter Grade: {grade}
    {encouraging_message}
""")


# =============================================================================
# Main Program
# =============================================================================

def main():
    """Main entry point for the quiz game."""
    # Create question bank
    questions = create_question_bank()
    
    # Run the quiz
    score, total = run_quiz(questions)
    
    # Display results
    display_results(score, total)
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ")
    if play_again.lower() in ["yes", "y"]:
        main()
    else:
        print("\nThanks for playing! Goodbye!")


if __name__ == "__main__":
    main()
