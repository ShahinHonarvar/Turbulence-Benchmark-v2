def lists_with_product_equal_n(nums):
    target_product = -8
    n = len(nums)
    result = []

    def find_sublists(start, current_product, current_list):
        if current_product == target_product:
            result.append(current_list.copy())
        if current_product != 0 and abs(current_product) > abs(target_product):
            return
        for i in range(1, n + 1):
            end = (start + i) % n
            next_product = current_product * nums[end]
            current_list.append(nums[end])
            find_sublists(end, next_product, current_list)
            current_list.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return result