def lists_with_product_equal_n(nums):

    def sublists_product_equal(nums, target):
        result = []
        n = len(nums)
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= nums[end % n]
                if product == target:
                    result.append(nums[start:end % n + 1])
                if product < target and product * nums[(end + 1) % n] > target:
                    break
        return result
    return sublists_product_equal(nums, -906)