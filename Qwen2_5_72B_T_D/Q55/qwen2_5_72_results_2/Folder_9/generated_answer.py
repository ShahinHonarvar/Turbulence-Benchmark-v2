def lists_with_product_equal_n(nums):

    def find_sublists(start, target, nums):
        n = len(nums)
        result = []
        current_product = 1
        for i in range(n):
            current_product *= nums[(start + i) % n]
            if current_product == target:
                result.append(nums[start:(start + i + 1) % n])
        return result
    all_results = []
    nums = nums + nums
    for i in range(len(nums) // 2):
        all_results.extend(find_sublists(i, -36, nums))
    return all_results