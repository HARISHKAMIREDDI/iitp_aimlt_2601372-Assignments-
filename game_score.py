"""Create a Python script named game_score.py that accomplishes the following:

Input Collection: Prompt the user to enter the player's name and store it as a string
Numeric Input Processing: Accept the number of games played and convert it to an integer data type
Score Data Entry: Collect the total score achieved and store it as an integer
Computation: Calculate the average score per game using division
Output Display: Present the results in the specified format shown below

Expected Output Format:
Player: <name>

Games Played: <number>

Total Score: <score>

Average Score: <average>"""

name=input("Enter the player's name: ")
games_played= int(input("Enter the number of games played: "))
total_score= int(input("Enter the total score achieved so far: "))
print(f"Player: {name}")
print(f"Games Played: {games_played}")
print(f"Total Score: {total_score}")
print(f"Average Score: {total_score/games_played}")