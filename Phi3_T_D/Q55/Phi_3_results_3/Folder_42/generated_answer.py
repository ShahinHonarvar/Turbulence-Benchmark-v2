from itertools import cycle

def lists_with_product_equal_n(circular_list):
    n = 25
    size = len(circular_list)
    result = []
    for i in range(size):
        current_product = 1
        temp_sublist = []
        for j in range(i, i + size):
            current_product *= circular_list[j % size]
            if current_product == n:
                temp_sublist.append(circular_list[j % size])
                result.append(temp_sublist.copy())
                break
            elif current_product > n:
                break
        if current_product == n:
            break
    return result