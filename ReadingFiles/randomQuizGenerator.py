#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 
   'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 
   'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta',
   'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing',
   'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 
   'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 
   'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
   'New York': 'Albany','North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 
   'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 
   'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 
   'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 
   'Vermont':'Montpelier',  'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    #Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt','w')
    answerKeyFile=open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    #Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20)+f'State Captials quiz(Form{quizNum+1})')
    quizFile.write('\n\n')
    states=list(capitals.keys())
    #print(states)
    random.shuffle(states)
    for questionNum in range(50):
        #print(states[questionNum])
        #Get right & wrong answer
        correctAnswer=capitals[states[questionNum]] #This loop will loop through the states in the shuffled states list, from states[0] to states[49], find each state in capitals, and store that state’s corresponding capital in correctAnswer.
        wrongAnswer=list(capitals.values()) #
       # print(wrongAnswer[wrongAnswer.index(correctAnswer)])
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer=random.sample(wrongAnswer,3)
        #print(wrongAnswer)
        answerOptions=wrongAnswer+[correctAnswer]
        #print(answerOptions)
        random.shuffle(answerOptions)
        # Write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. { answerOptions[i]}\n") 
            quizFile.write('\n')
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()