"""
 * Emre Bayazitoglu, 2023 (emre-samet61@hotmail.de)
 * Day 2 of Advent of Code 2022
 * Rock Paper Scissors
"""

strategyGuide = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
pointPerOutcome = {'Lose': 0, 'Draw': 3, 'Win': 6}
pointPerStrategy = {'Rock': 1, 'Paper': 2, 'Scissors': 3}


def readInput() -> list:
    roundsAsOneList = []
    with open("rpsFile.txt", 'r') as inputFile:
        linesAsList = inputFile.readlines()
        for oneRound in linesAsList:
            roundsAsOneList.append(
                oneRound.strip())  # every element of list represents a round of rock, paper, scissors
            # as a string
    return roundsAsOneList


def sumOfPoints(oneRound: list) -> int:
    sumPoints = 0
    for round in oneRound:
        goodElfChoice = strategyGuide[round[2]]
        opponentElvesChoice = strategyGuide[round[0]]
        if goodElfChoice == opponentElvesChoice:  # check draw cond.
            sumPoints += pointPerOutcome['Draw'] + pointPerStrategy[goodElfChoice]
        elif goodElfChoice == "Rock" and opponentElvesChoice == "Scissors" or goodElfChoice == "Scissors" \
                and opponentElvesChoice == "Paper" or goodElfChoice == "Paper" and opponentElvesChoice == "Rock":
            sumPoints += pointPerOutcome['Win'] + pointPerStrategy[goodElfChoice]  # check winning cond.
        else:  # else is losing cond.
            sumPoints += pointPerOutcome['Lose'] + pointPerStrategy[goodElfChoice]
    return sumPoints


print(sumOfPoints(readInput()))
# result = 14069
