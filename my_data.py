# Use old code to populate majority
def testGuess(user_guess="0", guess_count="0", random_number=0, user_name="Bob"):
    correctGuess = 0
    # Accepts numbers only
    if str.isnumeric(user_guess):
        # Check for the bounds
        if int(user_guess) < 1 or int(user_guess) > 100:
            print()
            print(" Integers from 1 to 100 only" )
            print()
        # Low Test
        elif int(user_guess) < random_number:
            guess_count = guess_count + 1
            print(f"{user_guess} is too low.  Guess again.")
        # High Test
        elif int(user_guess) > random_number:
            guess_count = guess_count + 1
            print(f"{user_guess} is too high.  Guess again.")
        # Correct Test
        else:
            guess_count = guess_count + 1
            print()
            print(f" {user_guess} IS CORRECT! ")
            print(f"It took you {guess_count} guesses, {user_name}!")
            print()
            correctGuess = 1
    # Have ability to quit
    elif user_guess.upper()[0] == "Q":
        correctGuess = 2
    # Only Integers
    else:
        print()
        print(" Integers from 1 to 100 only! ")
        print()
    return guess_count, correctGuess
def updateScores(playerName, numberOfGuesses):
# Create lists
    lines = []
    tlist = []
    quit = False
    # Use the code from Sorting Files assignment to help.
    # Use Try Block and have For loops inside.
    try:
        # Read in the .txt file (refer to sorting files)
        score_file = open("topPlayers.txt", "r")
        for each_line in score_file.readlines():
            lines.append(each_line)
        score_file.close()
        new_score = str(str(numberOfGuesses) + "          ")[0:10] + playerName
        lines.append(new_score)
        # Sort in score, name order. Only want last 10 digits of score. Refer to Sorting Files again here
        for unique_score in lines:
            [score, name] = unique_score.split(" ", 1)
            score = "0000000000" + score
            score = score[-10:]
            tlist.append(score + ":" + name.strip())
        tlist.sort()
        lines.clear()
        # Only want top 5 scores
        for unique_score in tlist[0:5]:
            [score, name] = unique_score.split(":")
            new_score = str(str(int(score)) + "          ")[0:10] + name
            lines.append(new_score)
        # Write the file
        score_file = open("topPlayers.txt", "w")
        for eachScore in lines:
            score_file.write(eachScore + " \n")
        score_file.close()
    # Remember except statement to close the try block
    except Exception as exception:
        quit = displayErrorMessage("An error has occurred. Sorry! ")
    finally:
        return quit
# Now for the display scores function
def displayScores():
    quit = False
    try:
        print("TOP PLAYERS LIST ")
        scores_file = open("topPlayers.txt", "r")
        scores = scores_file.read()
        scores_file.close()
        print(scores)
    except Exception as exception:
        quit = displayErrorMessage("An error has occurred. ")
    finally:
        return quit