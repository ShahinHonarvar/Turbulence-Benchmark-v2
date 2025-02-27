def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == -3:
            result.append(current[:])
        if product == 0 or abs(product) > 3:
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            if product * num == 0:
                continue
            current.append(num)
            find_sublists(i + 1, product * num, current, result)
            current.pop()
    result = []
    find_sublists(0, 1, [], result)
    return result