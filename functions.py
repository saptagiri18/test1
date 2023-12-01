import random
def getanswer(answerNumber):
    if answerNumber==1:
        return 'it is certain'
    elif answerNumber==2:
        return'ok hello'
    elif answerNumber==3:
        return 'ok how are you'
    elif answerNumber<=8:
        return ' es int'
print(getanswer(random.randint(1,9)))
