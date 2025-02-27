def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)

    def helper(start, product):
        if product == 6 or not nums:
            result.append(nums[start:] + nums[:start])
            return
        if product * nums[start] == 6:
            result.append(nums[start:])
            return
        for i in range(start, n + start):
            helper(i + 1, product * nums[i % n])
    helper(0, 1)
    return result