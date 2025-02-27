from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        current_product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            current_product *= circular_list[index]
            sublist.append(circular_list[index])
            if current_product == -36:
                result.append(sublist[:])
            if current_product != 0 and abs(current_product) > 36:
                break
    return result