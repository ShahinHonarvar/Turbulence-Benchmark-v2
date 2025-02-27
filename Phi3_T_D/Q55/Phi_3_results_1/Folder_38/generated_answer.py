from itertools import cycle

def lists_with_product_equal_n(circular_list):
    target_product = -23
    count = len(circular_list)
    sublists = []
    for start_idx in range(count):
        temp = [circular_list[start_idx]]
        product = circular_list[start_idx]
        for next_idx in cycle(range(count)):
            if next_idx == start_idx:
                break
            product *= circular_list[next_idx]
            temp.append(circular_list[next_idx])
            if product == target_product:
                sublists.append(temp[:])
            if any((sublist == temp[:] for sublist in sublists)):
                break
            if len(temp) > count:
                break
    return sublists