def lists_with_product_equal_n(nums):

    def helper(start, prod, path, result):
        if prod == 28:
            result.append(path[:])
            return
        if prod > 28:
            return
        for i in range(start, start + len(nums)):
            i = i % len(nums)
            prod *= nums[i]
            path.append(nums[i])
            helper(i + 1, prod, path, result)
            prod //= path.pop()
    result = []
    helper(0, 1, [], result)
    return result