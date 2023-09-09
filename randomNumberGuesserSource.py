import random
from colored import fg  

red = fg('light_red')
white = fg('white')
lightGreen = fg('light_green')
green = fg('green')
yellow = fg('yellow')

numRange = 0
boolRange = False
while boolRange is False:
    try:
        numRange = int(input(white + "Enter Range: "))
        if numRange < 0:
            print(red + "Only positive numbers are allowed!")
            print()
        else:
            boolRange = True
    except ValueError:
        print(red + "Whole Numbers only!")
        print()

number = random.randint(0, numRange)

print(number)

def compute1(number, multiplier):
    answer  = int(number * multiplier)
    return answer

def compute2(number, multiplier, multiplier2):
    if number > numRange * 0.5:
        temp = numRange - number
        answer = int(numRange - (temp * multiplier2))
    else:
        answer = int(number * multiplier)
    return answer

boolGuess = False
while boolGuess is False:
    try:
        guess = int(input(white + "Guess: "))
        '''
        num = 10
        Too Low = 20% or 0.2 
        Higher = 50% or 0.5
        You're close = 80% or 0.8
        Too High = 180% or 1.8
        Lower = 150% or 1.5
        You're close = 120% or 1.2

        FORMULA: ((num - diff(range)) * percentage)) + diff(range)
        
        NEW FORMULA
        if number is close to minimum:
            number - minimum = tempMin
            max - number = tempMax
            tooLow = (tempMin * 0.2) + 100
            higher = (tempMin * 0.5) + 100
            close1 = (tempMin * 0.8) + 100
            close2 = number + (tempMin * 0.8)
            lower = (tempMax * 0.5) + number
            tooHigh = (tempMax * 0.8) + number

        if number is close to maximum:
            maximum - number = tempMax
            number - minimum = tempMin
            tooLow = number - (tempMin * 0.8)
            higher = number - (tempMin * 0.5)
            close1 = max - (tempMax * 0.8)
            close2 = number - (tempMax - (tempMax * 0.8))
            lower = max - (tempMax * 0.5)
            tooHigh = number - (tempMax * 0.2)

        NEW NEW FORMULA:
            if number > range * 0.5:
                temp = range - number
                answer = range - (temp * multiplier)
            else:
                normal formula
        '''

        tooLow = compute1(number, 0.2)
        higher = compute1(number, 0.5)
        close1 = compute1(number, 0.8)
        close2 = compute2(number, 1.2, 0.8)
        lower = compute2(number, 1.5, 0.5)
        tooHigh = compute2(number, 1.8, 0.2)
        

        if guess not in range(0, numRange + 1):
            print(f"{red}Number should be in range: 0 - {numRange}")
            print()
        elif guess == number:
            print(f"{lightGreen}Your guess is correct: {guess}")
            print()
            boolGuess = True
        elif guess in range(close1, close2 + 1):
            print(green + "You're close!")
            print()
        elif guess in range(tooLow, higher + 1): # 10 = 4-7
            print(yellow + "Try Higher!" )
            print()
        elif guess in range(higher, close1 + 1): # 10 = 4-7
            print(yellow + "Try Higher!" )
            print()
        elif guess in range(close2, lower + 1):
            print(yellow + "Try Lower!")
            print()
        elif guess in range(lower, tooHigh + 1):
            print(yellow + "Try Lower!")
            print()
        elif guess >= tooHigh:
            print(red + "Guess is Too High!")
            print()
        elif guess <= tooLow: # 10 = < 3
            print(red + "Guess is Too Low!")
            print()
    except ValueError:
        print(red + "Whole Numbers only!")
        print()
        continue

print(white + "Thank you for Guessing!")

  
    




