from itertools import cycle

def helper(lst, current_product, current_sublist, n, visited):
    if current_product == n:
        return [current_sublist]
    results = []
    for item in zip(visited, cycle(lst)):
        if item[1] == 0 or item[0] != item[1]:
            new_visited = visited.copy()
            new_visited[lst.index(item[1])] = 0
            results.extend(helper(lst, current_product * item[1], current_sublist + [item[1]], n, new_visited))
    return results

def lists_with_product_equal_n(lst):
    n = -906
    if 0 in lst:
        lst_as_tuple = tuple(lst)
        if n % 0 == 0 and lst.count(0) < len(lst):
            return [[]]
    visited = [0] * len(lst)
    return helper(lst, 1, [], n, visited)