def lists_with_product_equal_n(nums):

    def helper(start, length):
        sublists = []
        for size in range(1, length + 1):
            temp_product = 1
            for i in range(size):
                temp_product *= nums[(start + i) % length]
            if temp_product == 0:
                sublists.append(nums[start:(start + size) % length])
            else:
                continue
        return sublists
    n = len(nums)
    result = []
    for i in range(n):
        result.extend(helper(i, n))
    return result