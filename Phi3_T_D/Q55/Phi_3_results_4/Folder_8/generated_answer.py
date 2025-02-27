from itertools import cycle

def lists_with_product_equal_n(circular_list, n):
    if n == 0:
        return [[]] if not circular_list else []
    result = []
    for i in range(len(circular_list)):
        sublists = []
        temp_product = 1
        for j in range(len(circular_list)):
            temp_product *= circular_list[(i + j) % len(circular_list)]
            if temp_product == n:
                sublists.append(circular_list[i:i + j + 1])
            elif temp_product > n:
                break
        result.extend(sublists)
    return result