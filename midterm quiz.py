#Daniel Pingrey
#12/19
#Midterm Quiz

import sys

def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        return file
    except IOError as e:
        print("Unable to open file:", file_name, "Ending program.\n")
        input("\n\nPress the enter key to exit")
        sys.exit()


def next_line(the_file):
    line = the_file.readline()
    line = line.strip("\n")
    line = line.replace("/", "\n")
    return line

def question_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation
        
def welcome(title):
    """Welcome the player to the test and get his/her name"""
    print("\t\nWelcome to the Python Trivial Challenge\n")
    print("\tThis test was created by", title, "\n")


def get_file_name():
    while True:
        file_name = input("Enter the name of your file, including the '.txt' at the end: ")
        if ".txt" in file_name and " " not in file_name:
            return file_name
        else:
            print("404 File Not Found")


def write_score(user_nameFull, score):
    file = open_file("scores.txt","a+")
    pair = user_nameFull+":   "+str(score)+"\n"
    line = []
    line.append(pair)
    file.writelines(line)
    file.close()

        
def main():
    file_name = get_file_name()
    file = open_file(file_name, "r")
    title = next_line(file)
    user_nameFull = input("Please enter your full name: ")
    question_count = 0
    score = 0
    category, question, answers, correct, explanation = question_block(file)
    welcome(title)
    while category:
        print(category)
        print()
        print(question)
        print()
        for i in range(len(answers)):
                       print(answers[i])
        user_answer = input("Answer: ")

        if user_answer == correct:
            print("\nCorrect")
            score += 1
            question_count += 1
        else:
            print("\nYou are wrong")
            question_count += 1
        print()
        print(explanation)
        category, question, answers, correct, explanation = question_block(file)
    file.close()
    print("And that was the final question")
    print("\nPress 'Enter' to view your score")
    report_card(user_nameFull, question_count, score)


def report_card(user_nameFull, question_count, score):
    print("\nEach question was worth 5 points, and this is how you did")
    print("\nReport Card")
    print("==============")
    print("Name:", user_nameFull)
    print("----")
    print("Questions answered:", question_count)
    print("----")
    print("Questions correct:", score)
    print("----")
    grade = (score / question_count) * 100
    

    A = """
     O~       
     O~ ~~     
    O~  O~~    
   O~~   O~~   
  O~~~~~~ O~~  
 O~~       O~~ 
O~~         O~~
"""
    
    B = """
O~~ O~~   
O~    O~~ 
O~     O~~
O~~~ O~   
O~     O~~
O~      O~
O~~~~ O~~
"""
    
    C = """
    O~~   
 O~~   O~~
O~~       
O~~       
O~~       
 O~~   O~~
   O~~~~
 """
    
    D = """
O~~~~~    
O~~   O~~ 
O~~    O~~
O~~    O~~
O~~    O~~
O~~   O~~ 
O~~~~~    
"""
    
    F = """
O~~~~~~~~
O~~      
O~~      
O~~~~~~  
O~~      
O~~      
O~~      
"""

    
    print(grade)
    
    if grade >= 90:
        print(A)
    elif grade < 90 and grade >= 80:
        print(B)
    elif grade < 80 and grade >= 70:
        print(C)
    elif grade < 70 and grade >= 60:
        print(D)
    elif grade < 60:
        print(F)
    
    print("==============")
    write_score(user_nameFull, grade)
    
main()
input("Press 'Enter' to close")




