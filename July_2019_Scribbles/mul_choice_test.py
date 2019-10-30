
from Question import Question
import time

question_prompts = [
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n',
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
    '<EOL>'
]

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time\'s up')

def run_test(questions, t):
    score = 0
    start = time.time()
    end = start + t
    # time.sleep(1)
    while time.time() < end:
        if time.time() > end:
            break
        else:
            for question in questions:
                answer = input(question.prompt)
                if time.time() > end or question == '<EOL>':
                    break
                elif answer == question.answer:
                    score +=1
            print('You got ' + str(score) + '/' + str(len(questions)) + ' correct')
    print('Time\'s up!')           

run_test(questions, 5)