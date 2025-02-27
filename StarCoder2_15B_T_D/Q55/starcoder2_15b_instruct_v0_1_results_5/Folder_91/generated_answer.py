def lists_with_product_equal_n(nums):

    def helper(nums, target, path, result):
        if target == 1:
            result.append(path)
            return
        for i in range(len(nums)):
            if target % nums[i] == 0:
                helper(nums, target // nums[i], path + [nums[i]], result)
    result = []
    helper(nums, 2, [], result)
    return result