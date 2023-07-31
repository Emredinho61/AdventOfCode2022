"""
 * Emre Bayazitoglu, 2023 (emre-samet61@hotmail.de)
 * Day 4 of Advent of Code 2022
 * Camp Cleanup
"""


def readAndParseInput(fileName: str) -> list:
    with open(fileName, "r") as inputFile:
        inputList = inputFile.readlines()
    inputList = [oneElement.strip().split(",") for oneElement in
                 inputList]  # get the input as [[min, max], [min2, max2],...]
    return inputList


def minMaxInput(inputList: list[list[list, list]]) -> list[list]:
    inputList = [
        [[int(sublistOfSublist.split('-')[0]), int(sublistOfSublist.split('-')[1])] for sublistOfSublist in sublist] for
        sublist in inputList]  # another parsing step
    return inputList


def contains(sublist1: list, sublist2: list) -> bool:
    if (sublist1[0] <= sublist2[0]) and (sublist1[1] >= sublist2[1]) or (sublist2[0] <= sublist1[0]) and (
            sublist2[1] >= sublist1[1]):  # check whether the first assignment completely includes the other assignment
        return True
    else:
        return False


def countContainings(inputList: list) -> int:
    count = sum([contains(sublist[0], sublist[1]) for sublist in minMaxInput(inputList)])
    return count


# print(countContainings(readAndParseInput("assignmentInput.txt")))
# result is 560 for part 1

####################### part 2 ################################


def checkOverlap(sublist1: list, sublist2: list) -> bool:
    if (sublist1[0] <= sublist2[0]) and (sublist1[1] >= sublist2[0]) or (
            (sublist2[0] <= sublist1[0]) and (sublist2[1] >= sublist1[0])):
        return True
    else:
        return False


def countOverlapping(inputList: list) -> int:
    count = sum([checkOverlap(sublist[0], sublist[1]) for sublist in minMaxInput(inputList)])
    return count


# print(countOverlapping(readAndParseInput("assignmentInput.txt")))
# 839 is the solution for part 2
