from math import log

def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] == nums[j]:
                continue
            sublist = nums[i:j + 1]
            if sum((log(abs(x)) for x in sublist)) == log(abs(15)):
                result.append(sublist if all((x != 0 for x in sublist)) else [])
    return result