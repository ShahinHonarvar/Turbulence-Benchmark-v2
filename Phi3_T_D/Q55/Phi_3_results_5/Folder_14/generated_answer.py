def lists_with_product_equal_n(circular_list, n=-72):
    result = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i, size + i):
            temp = circular_list[j % size]
            if temp != 0 and n % temp == 0:
                prod = temp
                sublist = [temp]
                for k in range(j + 1, (j + size) % size):
                    next_temp = circular_list[k % size]
                    if prod * next_temp == n:
                        prod *= next_temp
                        sublist.append(next_temp)
                    else:
                        break
                if prod == n:
                    result.append(sublist)
    return result