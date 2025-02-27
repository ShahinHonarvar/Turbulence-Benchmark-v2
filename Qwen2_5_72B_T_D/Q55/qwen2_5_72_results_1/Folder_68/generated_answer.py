def lists_with_product_equal_n(nums):

    def find_sublists(start, current_product, current_list):
        if current_product == 6:
            result.append(current_list)
            return
        if current_product > 6:
            return
        for i in range(start, start + len(nums)):
            find_sublists(i + 1, current_product * nums[i % len(nums)], current_list + [nums[i % len(nums)]])
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [])
    return [lst for lst in result if lst]