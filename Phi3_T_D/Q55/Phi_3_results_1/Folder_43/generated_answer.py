from itertools import cycle

def lists_with_product_equal_n(circular_list):
    target_product = -26
    result_sublists = []
    n = len(circular_list)
    for i in range(n):
        curr_product = 1
        sublist = []
        for j in range(i, i + n):
            curr_product *= circular_list[j % n]
            if curr_product == target_product:
                result_sublists.append(sublist)
            elif curr_product < 0 or curr_product > target_product:
                break
            sublist.append(circular_list[j % n])
            if len(sublist) >= n:
                break
    return result_sublists