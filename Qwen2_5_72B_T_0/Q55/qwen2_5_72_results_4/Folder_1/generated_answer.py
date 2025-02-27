def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == -51:
            result.append(current[:])
            return
        if start >= len(nums):
            return
        for i in range(start, len(nums)):
            if product * nums[i] <= -51:
                current.append(nums[i])
                find_sublists(i + 1, product * nums[i], current, result)
                current.pop()
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [], result)
        find_sublists(0, nums[i], [nums[i]], result)
    return result