#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 20:28
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : Bellman_Ford.py
# @Statement : The Bellman-Ford algorithm for the shortest path problem with edges of negative weights
# @Reference : Bellman R. On a routing problem[J]. Quarterly of Applied Mathematics, 1958, 16(1): 87-90.


def main(network, source):
    """
    The main function of the Bellman-Ford algorithm
    :param network: {node1: {node2: weights, node3: weights, ...}, ...}
    :param source: the source node
    :return:
    """
    # Step 1. Initialization
    nn = len(network)  # node number
    dis = [float('inf')] * nn  # the distance set
    path = [[]] * nn  # the path set
    dis[source] = 0
    path[source] = [source]

    # Step 2. The main loop
    for _ in range(nn - 1):
        for i in range(nn):
            if dis[i] != float('inf'):
                for j in network[i].keys():
                    if dis[i] + network[i][j] < dis[j]:
                        dis[j] = dis[i] + network[i][j]
                        temp_path = path[i].copy()
                        temp_path.append(j)
                        path[j] = temp_path

    # Step 3. Judge if the path contains a negative weight cycle
    for i in range(nn):
        if dis[i] != float('inf'):
            for j in network[i].keys():
                if dis[i] + network[i][j] < dis[j]:
                    print('The network contains negative weight cycles')
                    return
    return {'path': path, 'length': dis}


if __name__ == '__main__':
    source = 0
    # Example 1
    network1 = {
        0: {1: 6, 2: 5, 3: 5},
        1: {4: -1},
        2: {1: -2, 4: 1},
        3: {2: -2, 5: -1},
        4: {6: 3},
        5: {6: 3},
        6: {},
    }
    print(main(network1, source))

    # Example 2
    network2 = {
        0: {1: 4, 3: 4},
        1: {3: 4},
        2: {1: -10},
        3: {2: 3},
    }
    print(main(network2, source))
