from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        current_product = 1
        current_sublist = []
        for j in range(n):
            index = (i + j) % n
            current_product *= circular_list[index]
            current_sublist.append(circular_list[index])
            if current_product == 32:
                result.append(current_sublist.copy())
            if current_product > 32:
                break
    return result