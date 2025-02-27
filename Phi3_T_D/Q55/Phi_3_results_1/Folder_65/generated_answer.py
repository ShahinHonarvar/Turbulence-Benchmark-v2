def circular_shift(lst):
    return lst[1:] + lst[:1]

def lists_with_product_equal_n(lst, target=46):
    res = set()
    n = len(lst)
    for i in range(n):
        temp_res = []
        prod = 1
        for num in lst:
            if prod * num == target:
                temp_res.append(num)
                res.add(tuple(temp_res))
            elif prod * num > target:
                break
            else:
                prod *= num
                temp_res.append(num)
        lst = circular_shift(lst)
    return [list(sublist) for sublist in res]