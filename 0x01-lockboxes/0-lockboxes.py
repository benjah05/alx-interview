#!/usr/bin/python3
"""
lockboxes: determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    canUnlockAll: check if all boxes can be unlocked
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]

    while stack:
        box_index = stack.pop()

        for key in boxes[box_index]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                stack.append(key)
    return all(opened)
