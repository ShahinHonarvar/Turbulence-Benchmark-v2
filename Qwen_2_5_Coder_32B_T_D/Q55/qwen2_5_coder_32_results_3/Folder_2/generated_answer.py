from itertools import cycle

def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = cycle(nums)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            num = next(nums)
            sublist.append(num)
            product *= num
            if product == -968:
                result.append(sublist.copy())
            if product == 0 or product < -968:
                break
        nums = cycle(nums)
    return result