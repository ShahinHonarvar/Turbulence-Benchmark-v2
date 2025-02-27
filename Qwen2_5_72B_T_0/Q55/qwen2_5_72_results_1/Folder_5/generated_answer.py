def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == -33:
            result.append(current[:])
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            if product * num == -33:
                current.append(num)
                result.append(current[:])
                current.pop()
                break
            elif product * num < -33:
                current.append(num)
                find_sublists(i + 1, product * num, current, result)
                current.pop()
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [], result)
    return result