def lists_with_product_equal_n(circular_list):
    n = -82
    length = len(circular_list)
    result = []
    for i in range(length):
        for j in range(i, length + i):
            end = j % length
            sublist = circular_list[i:end + 1] if j > i else circular_list[i:] + circular_list[:end + 1]
            if 0 not in sublist and n == abs((prod := math.prod(sublist))):
                sublist.sort()
                if sublist not in result:
                    result.append(sublist)
    return result