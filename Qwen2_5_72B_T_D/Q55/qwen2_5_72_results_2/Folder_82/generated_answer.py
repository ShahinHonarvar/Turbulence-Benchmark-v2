def lists_with_product_equal_n(nums):
    target_product = 8
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = nums[start:start + end] + nums[:end - (n - start) if start + end > n else 0]
            if len(sublist) > 0 and all((isinstance(x, int) for x in sublist)) and (product(sublist) == target_product):
                result.append(sublist)
    return result

def product(lst):
    p = 1
    for num in lst:
        p *= num
    return p