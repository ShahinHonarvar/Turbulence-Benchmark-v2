def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == -56:
            result.append(current[:])
            return
        if start >= len(nums):
            return
        for i in range(start, len(nums)):
            if product * nums[i] == -56:
                result.append(current + [nums[i]])
            elif product * nums[i] != 0:
                find_sublists(i + 1, product * nums[i], current + [nums[i]], result)
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [], result)
        nums.insert(len(nums), nums.pop(0))
    return result