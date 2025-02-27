from collections import deque

def lists_with_product_equal_n(circular_list):

    def product(arr):
        p = 1
        for i in arr:
            p *= i
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = circular_list[start:start + size] if start + size <= n else circular_list[start:] + circular_list[:start + size - n]
            if product(sublist) == 10:
                result.append(sublist)
    return result