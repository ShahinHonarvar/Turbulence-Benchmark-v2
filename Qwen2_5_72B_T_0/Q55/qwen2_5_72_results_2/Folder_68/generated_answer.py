def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == 6:
            result.append(current[:])
            return
        if product > 6:
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            current.append(num)
            find_sublists(i + 1, product * num, current, result)
            current.pop()
    result = []
    find_sublists(0, 1, [], result)
    return result