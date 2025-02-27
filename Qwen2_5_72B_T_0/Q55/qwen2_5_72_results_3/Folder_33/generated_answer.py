def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -115
    result = []

    def find_sublists(start, current_product, current_list):
        if current_product == target_product:
            result.append(current_list.copy())
        if current_product == 0 or abs(current_product) > abs(target_product):
            return
        for i in range(1, n + 1):
            next_index = (start + i) % n
            find_sublists(next_index, current_product * nums[next_index], current_list + [nums[next_index]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result