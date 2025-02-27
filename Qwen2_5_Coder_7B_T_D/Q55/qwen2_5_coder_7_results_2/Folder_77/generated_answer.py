from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = 632
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for i in range(length):
            index = (start + i) % length
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:start + i + 1])
            elif product > n:
                break
    return result