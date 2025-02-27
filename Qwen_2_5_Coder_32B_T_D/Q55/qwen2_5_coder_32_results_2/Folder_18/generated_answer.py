from itertools import islice

def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            product *= nums[(start + i) % n]
            if product == 36:
                result.append(islice(nums, start, start + i + 1))
            elif product > 36:
                break
    return [list(sub) for sub in result]