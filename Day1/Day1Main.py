"""
 * Emre Bayazitoglu, 2023 (emre-samet61@hotmail.de)
 * Day 1 of Advent of Code 2022
 * Calorie Counting
"""


def computeMaxCalorie(filename: str) -> tuple[int, int]:  # first int is id of elve with max(cal), second is max(cal)
    caloriePerElfList = readInput(filename)
    currentMax = 0
    maxId = 0
    resultTuple = ()
    for oneElve in caloriePerElfList:
        if currentMax <= sum(oneElve[1]):  # oneElve[1] holds a sublist with calories per elve
            currentMax = sum(oneElve[1])
            maxId = oneElve[0]
        resultTuple = (maxId, currentMax)  # oneElve[0] holds the id of elve
    return resultTuple


def readInput(filename: str) -> list[tuple[int, list[int]]]:
    with open(filename) as f:
        caloriesPerElf = f.read().split("\n\n")  # list entries are separated by double returns
    # for every element in list change type to int, after removing return. Then enumerate list elements in order to get
    # id of every elf.
    return list(enumerate([list(map(int, oneElf.strip().split("\n"))) for oneElf in caloriesPerElf]))


if __name__ == "__main__":
    input_path = "calorieFile.txt"
    print("(id of elf, total of calories)")
    print(computeMaxCalorie(input_path))
