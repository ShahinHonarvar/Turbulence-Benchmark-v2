def lists_with_product_equal_n(nums):
    target_product = 714
    n = len(nums)
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist[:])
            return
        if product > target_product:
            return
        for i in range(start, start + n):
            num = nums[i % n]
            find_sublists(i + 1, product * num, sublist + [num])
    for i in range(n):
        find_sublists(i, 1, [])
    return result