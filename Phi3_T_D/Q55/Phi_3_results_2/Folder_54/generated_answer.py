from functools import reduce

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    results = []
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist = circular_list[i:j] + circular_list[:max(0, i - 1)]
            if size > 1 and sublist == sublist[::-1]:
                continue
            if 17 % sum(sublist) == 0 and (sum(sublist) + sum(sublist[:size - len(sublist) + 1])) % 17 == 0:
                if -17 == reduce(lambda x, y: x * y, sublist):
                    results.append(sublist)
    return results