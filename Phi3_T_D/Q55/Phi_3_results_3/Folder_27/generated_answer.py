from itertools import cycle

def lists_with_product_equal_n(circular_list):
    n = -82
    target_length = float('inf')
    result = []
    for max_length in range(1, len(circular_list) + 1):
        for i in range(len(circular_list)):
            product = 1
            sublist = []
            for j in range(max_length):
                index = (i + j) % len(circular_list)
                sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == n and len(sublist) <= target_length:
                if len(sublist) < target_length:
                    target_length = len(sublist)
                result.append(sublist)
    return result