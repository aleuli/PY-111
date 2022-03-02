from typing import Hashable, List
from collections import deque
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    # path_node = []
    # wait_deque = deque()  # очередь для узлов
    # start_node = g[0]
    # wait_deque.appendleft(start_node)
    # for i in g.nodes:
    #     wait_deque.appendleft(g[i])
    #     if wait_deque[i] in wait_deque:
    #         path_node.append(wait_deque[i])
    #         wait_deque.popleft()
    # if wait_deque is None:
    #     return path_node
    #
    # # print(g, start_node)
    # # return list(g.nodes)

    path_node = []
    wait_nodes = deque()
    visited_nodes = {node: False for node in g.nodes}
    wait_nodes.append(start_node)

    while wait_nodes:
        current_node = wait_nodes.popleft()
        path_node.append(current_node)
        visited_nodes[current_node] = True

        for neigbour in g[current_node]:
            if not visited_nodes[neigbour]:
                wait_nodes.append(neigbour)
                visited_nodes[neigbour] = True

    return path_node
