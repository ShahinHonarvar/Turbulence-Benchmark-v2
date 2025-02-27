from math import prod

def lists_with_product_equal_n(nums):

    def circular_sublist(lst, start, length):
        return [lst[i % len(lst)] for i in range(start, start + length)]
    target_product = -56
    result = []
    for i in range(len(nums)):
        for j in range(1, len(nums) + 1):
            sublist = circular_sublist(nums, i, j)
            if len(sublist) > 0 and all((isinstance(x, int) for x in sublist)) and (sum([0 if x == 0 else 1 for x in sublist]) > 0):
                if abs(prod(sublist) - target_product) < 1e-06:
                    result.append(sublist)
    return result