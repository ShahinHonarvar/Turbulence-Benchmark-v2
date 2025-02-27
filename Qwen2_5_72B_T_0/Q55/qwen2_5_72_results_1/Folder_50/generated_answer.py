def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = 45
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist.copy())
            return
        if product > target_product:
            return
        for i in range(start, start + n):
            num = nums[i % n]
            if product * num > target_product:
                continue
            sublist.append(num)
            find_sublists(i + 1, product * num, sublist)
            sublist.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return result