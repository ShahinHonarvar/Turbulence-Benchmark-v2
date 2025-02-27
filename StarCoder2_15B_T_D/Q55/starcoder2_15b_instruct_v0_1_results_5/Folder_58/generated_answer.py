def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = nums[i:j]
            if len(sublist) <= n and prod(sublist) == 733:
                result.append(sublist)
    return result

def prod(nums):
    result = 1
    for num in nums:
        result *= num
    return result