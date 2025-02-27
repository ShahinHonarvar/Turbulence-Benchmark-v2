def lists_with_product_equal_n(nums):
    target_product = 51
    n = len(nums)
    results = []

    def find_sublists(start, end):
        if start == end:
            if nums[start] == target_product:
                results.append([nums[start]])
            return
        current_product = 1
        for i in range(start, end + 1):
            current_product *= nums[i % n]
            if current_product == target_product:
                results.append(nums[start:i + 1])
            elif current_product > target_product:
                break
    for i in range(n):
        find_sublists(i, i + n - 1)
    return results