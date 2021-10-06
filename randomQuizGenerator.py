#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

   # Generate 35 quiz files.
for quizNum in range(35):
       # Create the quiz and answer key files.
        quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
        answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

       # Write out the header for the quiz.
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
        quizFile.write('\n\n')

       # Shuffle the order of the states.
        states = list(capitals.keys()) #create a list called states
        random.shuffle(states) #randomly reorders the values in the list passed to it (states)

       # Loop through all 50 states, making a question for each.
        for questionNum in range(50):
           # Get right and wrong answers.
                correctAnswer = capitals[states[questionNum]] #correct answer stored in capitals dictionary
           #will loop thru the states in the shuffled states list, from states[0] to states[49]
           #find each state in capitals and store the state's corresponding capital in correctAnswer
                wrongAnswers = list(capitals.values()) #duplicate all the values in the capitals dictionary
                del wrongAnswers[wrongAnswers.index(correctAnswer)] #delete the correct answer
                wrongAnswers = random.sample(wrongAnswers, 3) #select 3 ranodm values from the list
                answerOptions = wrongAnswers + [correctAnswer] #full list of answer options
                random.shuffle(answerOptions) #answers need to be randomized so that the correct response isn't always choice D

           # Write the question and answer options to the quiz file.
                quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
                for i in range(4):
                        quizFile.write(f"    {'ABCD'[i]}. { answerOptions[i]}\n") #answerOptions list, 'ABCD'[i] treats the string 'ABCD' as an array & will evaluate to 'A','B','C' and then 'D' on each respective iteration thru the loop
                        quizFile.write('\n')

           # Write the answer key to a file.
                answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}") #writing to the answer key file, the correct answer, will find the integer index of the correct answer
        quizFile.close()
        answerKeyFile.close()