from functools import reduce
    from operator import mul

def lists_with_product_equal_n(circular_list):
    circular_list *= 2
    target = 714
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            sublist = circular_list[i:j]
            if sum(sublist) <= len(circular_list) // 2 and prod(sublist) == target:
                result.append(sublist)
    return [list(x) for x in set((tuple(x) for x in result))]

def prod(lst):
    return reduce(mul, lst)