#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    boxes: list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    opened = [False] * len(boxes)
    opened[0] = True
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key > 0 and key < len(boxes) and not opened[key]:
                opened[key] = True
                stack.append(key)
    return all(opened)
