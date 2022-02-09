"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self.stack.append(elem)

        print(elem)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        if not self.stack:
            return None
        self.stack.pop()
        return None

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """
        # if len(self.stack) < 1:
        #     return None
        # count = 0
        # for i in self.stack[::-1]:
        #     if count == ind:
        #         return i
        #     count += 1
        ...  # когда нельзя достать элемент

        reversed_index = reversed(self.stack)
        reversed_index = -ind - 1
        return self.stack[reversed_index]

    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.stack.clear()
        return None