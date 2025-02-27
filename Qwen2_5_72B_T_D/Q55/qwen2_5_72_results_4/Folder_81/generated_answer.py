def lists_with_product_equal_n(nums):

    def sublists_with_product(nums, n, product):
        result = []
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j % len(nums)]
                if prod == product:
                    result.append(nums[i:j + 1])
                elif prod < product and j < len(nums) - 1:
                    continue
                else:
                    break
        return result
    product = -8
    result = sublists_with_product(nums, len(nums), product)
    circular_result = sublists_with_product(nums + nums, len(nums) * 2, product)
    final_result = [sub for sub in circular_result if len(sub) <= len(nums)]
    return final_result