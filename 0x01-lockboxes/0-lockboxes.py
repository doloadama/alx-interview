#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)
