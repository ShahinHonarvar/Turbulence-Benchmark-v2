def lists_with_product_equal_n(nums):
    target_product = 78
    n = len(nums)
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist.copy())
            return
        if product > target_product:
            return
        for i in range(n):
            next_index = (start + i) % n
            if next_index == start:
                continue
            find_sublists(next_index, product * nums[next_index], sublist + [nums[next_index]])
    for i in range(n):
        find_sublists(i, nums[i], [nums[i]])
    return result