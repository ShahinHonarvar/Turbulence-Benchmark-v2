def lists_with_product_equal_n(nums):

    def sublists_with_product(nums, target):
        n = len(nums)
        result = []
        for start in range(n):
            product = 1
            for end in range(n):
                product *= nums[(start + end) % n]
                if product == target:
                    result.append(nums[start:(start + end + 1) % n])
                elif product < target:
                    continue
                else:
                    break
        return result
    return sublists_with_product(nums, -89)