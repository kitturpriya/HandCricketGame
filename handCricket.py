import random
##name = input("Enter your name:\n")
##rules = (f"Welcome to the game {name}") 
## RULES
print('''The rules of the game are:
      1. There will be a toss between you and the computer, you have to chose either odd or even, after that you should put a number between 1 to 10
    if the sum of your and the computer's number is odd or even, accordingly to what you have choosen you will either win or loss the toss.
    If you win the toss you can either bat or bowl, and the same thing will happen with the computer.
    2. If you are batting then you have to put a number between 1 to 10 to score runs, if the number you have put and the number computer has put is same
    the you will be declared out, if not then you can continue to bat till you get out and it is a 10 over game
    3. After you finish batting, you have to bowl and defend your score and get the computer out be chosing the same number as the computer
    4. This is the beginning of your successful cricket journey
    5.Hope you have fun''')
SumValue = "junk"
print("Welcome to Hand Cricket, a new era of cricket for kids")
randnum = random.randint(1,10)
## TOSS
toss = input("Welcome to the toss, please choose either odd(o) or even(e):\n").lower()
tossNum = int(input("Please choose a number between 1 to 10:\n"))
if (tossNum>10 or tossNum<1):
    print("Invalid Input, ERROR 402 :(")
else:
    print(f"You chose {tossNum} and the computer chose {randnum}")
    sumToss = tossNum + randnum
    if (sumToss%2) == 0:
        SumValue = "e"
        print("It's even")
    else:
        SumValue = "o"   
        print("It's odd")
## PLAYER WON TOSS, CHOSE FOR BAT OR BOWL(EVEN/ODD)
if SumValue == toss:
    batbowl = input("You have won the toss, would you like to bat(b) or bowl(bo)")
    ## PLAYER WON TOSS AND CHOOSES TO BAT
    ## 1ST INNINGS
    if batbowl == "b":
        balls = 60
        ballsBat = 0
        playerRuns = 0
        print("-----------------------------------\nYour batting\n")
        while ballsBat < balls:
            Runs = int(input("Enter a number to bat: "))
            compBowl = random.randint(1,10)
            
            if Runs==compBowl:
                print(f"Your number is {Runs}, Computer's number is {compBowl}")
                print(f"You are Out. Your total score is {playerRuns}\n")
                break
            elif Runs>10:
                print("ERROR 408 :( , PLEASE TRY INPUTTING A NUMBER BELOW 11")
                continue
            else:
                playerRuns += Runs
                print(f"Your number: {Runs}, Computer's number: {compBowl}")
                print(f"Your runs now are {playerRuns}\n")
            
            ballsBat += 1
            
        ## COMPUTER BATTING
        ## 2ND INNINGS
        print("-----------------------------------\nComputer batting\n")
        balls2 = 60
        ballsBat2 = 0
        compRuns2 = 0
        while ballsBat2 < balls2:
            bowl2 = int(input("Enter runs to bowl: "))
            compBat2 = random.randint(1,11)
            
            if compBat2 == bowl2:
                print(f"Computer's number is {compBat2}, Your number is {bowl2}")
                print(f"Computer is Out. Computer's total runs are {compRuns2}")
                break
            else:
                compRuns2 += compBat2
                print(f"Computer's number is {compBat2}, Your number is {bowl2}")
                print(f"Computer's score is {compRuns2}\n")
                
                if compRuns2 > playerRuns:
                    break
            ballsBat2 += 1
            
        ## RESULTS
        print("-----------------------------------\nRESULTS: ")
            
        if compRuns2 < playerRuns:
            print(f"\nYou have won the game. \n\nYour total runs are {playerRuns} in {ballsBat} balls and the computer scored {compRuns2} in {ballsBat2} bowls")
        elif compRuns2 == playerRuns:
            print(f"The game is a tie, You score {playerRuns} and the computer also scored {compRuns2}")
        else:
            print(f"\nComputer won the game.\n\nComputer's total runs are {compRuns2} in {ballsBat2} bowls, and you score {playerRuns}")
    
    ## PLAYER WON TOSS AND CHOOSES TO BOWL
    ## 1ST INNINGS
    if batbowl == "bo":
        print("-----------------------------------\nComputer batting\n")
        balls3 = 60
        ballsBat3 = 0
        compRuns3 = 0
        while ballsBat3 < balls3:
            bowl3 = int(input("Enter runs to bowl: "))
            compBat3 = random.randint(1,10)
            
            if compBat3 == bowl3:
                print(f"Computer's number is {compBat3}, Your number is {bowl3}")
                print(f"Computer is Out. Computer's total runs are {compRuns3}")
                break
            else:
                compRuns3 += compBat3
                print(f"Computer's number is {compBat3}, Your number is {bowl3}")
                print(f"Computer's score is {compRuns3}\n")
            ballsBat3 += 1
        
        ## PLAYER BATTING
        ## 2ND INNINGS
        balls4 = 60
        ballsBat4 = 0
        playerRuns4 = 0
        print("-----------------------------------\nYour batting\n")
        while ballsBat4 < balls4:
            Runs4 = int(input("Enter a number to bat: "))
            compBowl4 = random.randint(1,10)
            
            if Runs4==compBowl4:
                print(f"Your number is {playerRuns4}, Computer's number is {compBowl4}")
                print(f"You are Out. Your total score is {Runs4}\n")
                break
            elif Runs4>10:
                print("ERROR 408 :( ---------INPUT A NUMBER BELOW 11")
                continue
            else:
                playerRuns4 += Runs4
                print(f"Your number: {Runs4}, Computer's number: {compBowl4}")
                print(f"Your runs now are {playerRuns4}\n")

                if playerRuns4 > compRuns3:
                    break
            ballsBat4 += 1
        print("-----------------------------------\nRESULTS: ")
                
        if compRuns3 < playerRuns4:
            print(f"\nYou have won the game. \n\nYour total runs are {playerRuns4} and Bowls taken(Out of 60) are {ballsBat4}\n Computer's total runs are {compRuns3}")
        elif compRuns3 == playerRuns4:
            print(f"The game is a tie, You score {playerRuns4} and the computer also scored {compRuns3}")
        else:
            print(f"\nComputer won the game.\n\nComputer's total runs are {compRuns3} and in {ballsBat3} balls and your runs are {playerRuns4}")
## COMPUTER WON THE TOSS AND CHOOSES TO BAT      
else: 
    ## COMPUTER BATTING 
    ## 1ST INNINGS
    print("Computer has won the toss and it chooses to bat first\n")
    print("-----------------------------------\nComputer batting\n")
    balls3 = 60
    ballsBat3 = 0
    compRuns3 = 0
    while ballsBat3 < balls3:
        bowl3 = int(input("Enter runs to bowl: "))
        compBat3 = random.randint(1,10)
        
        if compBat3 == bowl3:
            print(f"Computer's number is {compBat3}, Your number is {bowl3}")
            print(f"Computer is Out. Computer's total runs are {compRuns3}")
            break
        else:
            compRuns3 += compBat3
            print(f"Computer's number is {compBat3}, Your number is {bowl3}")
            print(f"Computer's score is {compRuns3}\n")
        ballsBat3 += 1
    
    ## COMPUTER BATTING
    ## 2ND INNINGS
    balls4 = 60
    ballsBat4 = 0
    playerRuns4 = 0
    print("-----------------------------------\nYour batting\n")
    while ballsBat4 < balls4:
        Runs4 = int(input("Enter a number to bat: "))
        compBowl4 = random.randint(1,10)
        
        if Runs4==compBowl4:
            print(f"Your number is {playerRuns4}, Computer's number is {compBowl4}")
            print(f"You are Out. Your total score is {Runs4}\n")
            break
        elif Runs4>10:
            print("ERROR 408 :( , PLEASE TRY INPUTTING A NUMBER BELOW 11")
            continue
        else:
            playerRuns4 += Runs4
            print(f"Your number: {Runs4}, Computer's number: {compBowl4}")
            print(f"Your runs now are {playerRuns4}\n")

            if playerRuns4 > compRuns3:
                break
        ballsBat4 += 1
    print("-----------------------------------\nRESULTS: ")
            
    if compRuns3 < playerRuns4:
        print(f"\nYou have won the game. \n\nYour total runs are {playerRuns4} and Bowls taken(Out of 60) are {ballsBat4}\n Computer's total runs are {compRuns3}")
    elif compRuns3 == playerRuns4:
        print(f"The game is a tie, You score {playerRuns4} and the computer also scored {compRuns3}")
    else:
        print(f"\nComputer won the game.\n\nComputer's total runs are {compRuns3} and in {ballsBat3} balls and your runs are {playerRuns4}")
        
input("Press any key to exit")