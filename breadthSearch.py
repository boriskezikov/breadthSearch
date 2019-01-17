import re
from queue import Queue


def breadth_search(dataR):
    data = []
    with open(dataR, "r", encoding="utf-8") as file:
        if file:
            for line in file.readlines():
                new_line = re.sub('\n','', line)
                new_line = re.sub(' ','',new_line)
                data.append(new_line)

    matrix = [element for element in data if len(element) > 3]
    start_point = int(data[len(data) - 1][0])-1
    finish_point = int(data[len(data) - 1][1])-1


    queue = Queue()
    queue.put(matrix[start_point])
    visited = []
    while not queue.empty():
        current_point = queue.get()
        if current_point != matrix[finish_point]:
            if current_point in visited:
                continue
            for i in range(len(current_point)):
                    if int(current_point[i]) == 1:
                        queue.put(matrix[int(i)])
            visited.append(current_point)
        else:
            break
    visited.append(matrix[finish_point])
    matrix_dict = {matrix[i]: i for i in range(len(matrix))}
    for i in visited:
        print(matrix_dict[i])


breadth_search("/Users/kezikovboris/Desktop/graph.txt")
