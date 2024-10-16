questions = [
    {
        "question": "What is the video game that won Game of the Year in 2015",
        "options": ["Fallout 4", "Super Mario Maker", "The Witcher 3: Witch Hunt", "Bloodborne"],
        "correct_answer": "The Witcher 3: Witch Hunt"
    },
    {
        "question": "On the periodic table, what does the element S represent?",
        "options": ["Sulfur", "Samarium", "Selenium", "Scandium"],
        "correct_answer": "Mars"
    },
    {
        "question": "Other than Steph Curry, who has made the most 3-pointers of all time in the NBA?",
        "options": ["Damien Lillard", "James Harden", "Reggie Miller", "Ray Allen"],
        "correct_answer": "Ray Allen"
    }
]

def run_quiz():
    score = 0
    correct_answers = []
    incorrect_answers = []
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, option in enumerate(question['options'], 1):
            print(f"{j}.{option}")

        while True:
            user_answer = input("Select the number for your answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <=len(question['options']):
                user_answer = question['options'][int(user_answer) - 1]
                break
            else:
                print("Invalid response. Please enter a number corresponding to the options of the question.")
        
        if user_answer == question['correct_answer']:
            score += 1
            correct_answers.append(question['question'])
        else:
            incorrect_answers.append((question['question'], user_answer, question['correct_answer']))
            
    print("\n---Trivia Complete---")