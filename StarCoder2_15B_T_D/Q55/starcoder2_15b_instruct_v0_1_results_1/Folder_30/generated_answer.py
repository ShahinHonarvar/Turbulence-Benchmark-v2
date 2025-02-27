def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            sublist = nums[i:j]
            if len(sublist) <= n and product(sublist) == 99:
                result.append(sublist)
    return result

def product(nums):
    res = 1
    for num in nums:
        res *= num
    return res