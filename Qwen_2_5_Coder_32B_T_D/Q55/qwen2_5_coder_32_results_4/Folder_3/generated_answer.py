def lists_with_product_equal_n(lst):

    def find_sublists_with_product(target, nums):
        result = []
        n = len(nums)
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= nums[end % n]
                if product == target:
                    result.append(nums[start % n:end % n + 1])
                if product == 0 or product % target != 0:
                    break
        return result
    return find_sublists_with_product(-22, lst)