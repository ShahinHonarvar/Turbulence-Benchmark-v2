def lists_with_product_equal_n(circular_list):

    def get_sublists(nums, target_product):
        n = len(nums)
        result = []
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= nums[end % n]
                if product == target_product:
                    result.append(nums[start:end % n + 1])
                elif product < -100:
                    break
        return result
    return get_sublists(circular_list, -89)