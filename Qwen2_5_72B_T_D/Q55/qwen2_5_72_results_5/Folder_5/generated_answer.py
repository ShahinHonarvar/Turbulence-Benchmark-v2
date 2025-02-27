def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == -33:
            result.append(current[:])
            return
        for i in range(start, start + len(nums)):
            i = i % len(nums)
            if nums[i] * product == 0:
                continue
            current.append(nums[i])
            find_sublists(i + 1, product * nums[i], current, result)
            current.pop()
    result = []
    find_sublists(0, 1, [], result)
    return result