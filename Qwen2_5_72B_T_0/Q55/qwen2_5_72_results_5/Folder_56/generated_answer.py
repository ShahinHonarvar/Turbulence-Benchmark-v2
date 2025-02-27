def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == -65:
            result.append(current[:])
            return
        if start >= len(nums):
            return
        for i in range(start, len(nums)):
            if product * nums[i] == -65:
                current.append(nums[i])
                result.append(current[:])
                current.pop()
            elif product * nums[i] != 0:
                current.append(nums[i])
                find_sublists(i + 1, product * nums[i], current, result)
                current.pop()
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [], result)
    return result