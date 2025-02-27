def lists_with_product_equal_n(nums):

    def find_sublists(nums, target, start_idx=0):
        results = []
        for i in range(start_idx, len(nums)):
            product = 1
            for j in range(i, len(nums) + i):
                product *= nums[j % len(nums)]
                if product == target:
                    results.append(nums[i:(j + 1) % len(nums)])
        return results
    return find_sublists(nums, -91)