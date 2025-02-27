def lists_with_product_equal_n(nums):

    def helper(nums, start, end, target, current, result):
        if start % len(nums) == end:
            return
        current.append(nums[end])
        product = 1
        for num in current:
            product *= num
        if product == target:
            result.append(list(current))
        helper(nums, start, (end + 1) % len(nums), target, current, result)
        current.pop()
        helper(nums, start, (end + 1) % len(nums), target, current, result)
    result = []
    for i in range(len(nums)):
        helper(nums, i, i, -61, [], result)
    return result