"""
 * Emre Bayazitoglu, 2023 (emre-samet61@hotmail.de)
 * Day 3 of Advent of Code 2022
 * Calorie Counting
"""


def getInputAsList(fileName: str) -> list:
    resultList = []
    with open(fileName, 'r') as input:
        inputAsList = input.readlines()
    for oneString in inputAsList:
        resultList.append(oneString.strip())  # remove \n from every listelement
    return resultList


def prioOfItems(item: str) -> int:
    if "a" <= item <= "z":
        return 1 + (ord(item) - ord("a"))  # priority for this one starts at 1 and ends at 26
    if "A" <= item <= "Z":
        return 27 + (ord(item) - ord("A"))  # priority for this one starts at 27 and ends at 52


def totalPart1(fileName: str) -> int:
    sumPrio = 0
    rest = []
    items = getInputAsList(fileName=fileName)
    for item in items:
        middle = len(item) // 2  # get the index of the middle objects in order to calculate prio
        for i in range(middle, len(item)):
            if item[i] in item[:middle]:
                rest.append(item[i])
        sumPrio += prioOfItems(rest.pop())  # extract single char, than processing it into sum
    return sumPrio


# i did solve part two aswell, but im not really happy with the amount of code i wrote, so i dont release it on the
# internet :) for part2 the result is 2681


print(totalPart1("rucksackInput.txt"))
# result: 8349
