def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -779
    result = []

    def helper(start, product, sublist):
        if product == target_product:
            result.append(sublist.copy())
            return
        if product != 0 and target_product % product != 0:
            return
        for i in range(1, n + 1):
            next_index = (start + i - 1) % n
            helper(next_index, product * nums[next_index], sublist + [nums[next_index]])
    for i in range(n):
        helper(i, 1, [])
    return result