def lists_with_product_equal_n(nums):
    target_product = -22
    n = len(nums)
    result = []

    def find_contiguous_subarrays(start, end, current_product):
        if current_product == target_product:
            result.append(nums[start:end])
            return
        if end - start >= n or end >= n:
            return
        find_contiguous_subarrays(start, end + 1, current_product * nums[end % n])
        if start == end:
            return
        find_contiguous_subarrays(start + 1, end, current_product // nums[start % n])
    for i in range(n):
        find_contiguous_subarrays(i, i, 1)
    return result