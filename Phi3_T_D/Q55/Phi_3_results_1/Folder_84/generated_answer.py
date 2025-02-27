def lists_with_product_equal_n(circular_list):
    target = -906
    n = len(circular_list)
    possible_sublists = []
    for i in range(n):
        prod = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            prod *= circular_list[index]
            if prod == target:
                sublist = circular_list[i:i + j + 1]
                possible_sublists.append(sublist)
                break
            elif prod > target:
                break
    return possible_sublists