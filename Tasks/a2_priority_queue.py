"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

# начало справа конец слева
class PriorityQueue:
    def __init__(self):
        self.quenue_priority = []

    def enqueue(self, elem: Any, priority: int = 0) -> None:  # O(N)
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        enqueue_item = {
            "value": elem,
            "priority": priority
        }
        if not self.quenue_priority:
            self.quenue_priority.append(enqueue_item)
        for index, current_item in enumerate(self.quenue_priority):
            if current_item["priority"] >= enqueue_item["priority"]:
                self.quenue_priority.insert(index, enqueue_item)
                break
            if index == len(self.quenue_priority) - 1:  # Если дошли до конца очереди и не нашли
                self.quenue_priority.append(enqueue_item)

    def dequeue(self) -> Any:  # O(1)
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.quenue_priority:
            return None

        return self.quenue_priority.pop()

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        ...

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.quenue_priority.clear()

