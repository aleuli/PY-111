"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []  # начало очереди слева , конец очереди справа

    def enqueue(self, elem: Any) -> None:  # O(1)
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.queue.append(elem)

    def dequeue(self) -> Any:  # O(N)
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.queue:
            return None

        value = self.queue[0]
        del self.queue[0]
        return value

    def peek(self, ind: int = 0) -> Any:  # O(N)
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if ind > len(self.queue):
            return None
        return self.queue[ind]

    def clear(self) -> None:  # O(1)
        """
        Clear my queue

        :return: None
        """
        self.queue.clear()
