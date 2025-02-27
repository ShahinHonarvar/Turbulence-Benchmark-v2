def lists_with_product_equal_n(nums):
    target_product = -61
    n = len(nums)
    result = []

    def find_sublists(start, end, product, current_sublist):
        if product == target_product:
            result.append(current_sublist.copy())
        if product == 0 or abs(product) > abs(target_product):
            return
        for i in range(start, end + 1):
            product *= nums[i % n]
            current_sublist.append(nums[i % n])
            find_sublists(i + 1, end, product, current_sublist)
            current_sublist.pop()
            product //= nums[i % n]
    for i in range(n):
        find_sublists(i, i + n - 1, 1, [])
    return result