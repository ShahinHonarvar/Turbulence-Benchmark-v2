def circular_shift(lst):
    return lst[1:] + lst[:1]

def lists_with_product_equal_n(lst):
    n = -56
    length = len(lst)
    result = []
    for i in range(length):
        product = 1
        sublist = []
        for j in range(i, i + length):
            index = j % length
            product *= lst[index]
            sublist.append(lst[index])
            if product == n:
                result.append(sublist.copy())
                break
            elif product > n:
                break
        if product == n:
            sublist = []
            reverse_product = 1
            for j in range(i + length - 1, i - 1, -1):
                index = j % length
                reverse_product *= lst[index]
                sublist.insert(0, lst[index])
                if reverse_product == n:
                    result.append(sublist.copy())
                    break
                elif reverse_product > n:
                    break
    return result