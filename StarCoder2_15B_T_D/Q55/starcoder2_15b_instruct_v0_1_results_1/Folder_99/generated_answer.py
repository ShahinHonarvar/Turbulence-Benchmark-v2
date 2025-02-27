def lists_with_product_equal_n(nums):
    n = len(nums)
    res = []
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist = nums[i:j]
            if len(sublist) > n:
                break
            if len(sublist) > 0 and len(sublist) <= n and (415 % prod(sublist) == 0):
                res.append(sublist)
    return res

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p