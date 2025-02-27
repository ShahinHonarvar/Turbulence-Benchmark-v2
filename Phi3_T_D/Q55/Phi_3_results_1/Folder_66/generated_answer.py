def rotate_list(lst, steps):
    for _ in range(steps):
        lst.insert(0, lst.pop())
    return lst

def find_sublists(lst, target_product, start_index=0, path=[]):
    if start_index >= len(lst):
        return [path] if isinstance(path, list) and prod(path) == target_product else []
    result = find_sublists(lst, target_product, start_index + 1, path + [lst[start_index]])
    if sum(path) > 0 and prod(path) * lst[start_index] > target_product:
        break
    else:
        path = [lst[start_index]]
        result += find_sublists(lst, target_product, start_index + 1, path)
    return result

def prod(lst):
    result = 1
    for i in lst:
        result *= i
    return result

def lists_with_product_equal_n(circular_list):
    result = []
    while True:
        sublists = find_sublists(circular_list, 78)
        if not sublists:
            break
        for sublist in sublists:
            if sublist not in result:
                result.append(sublist)
        circular_list = rotate_list(circular_list, 1)
    return result