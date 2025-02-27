def lists_with_product_equal_n(nums):

    def find_sublists(nums, target):

        def backtrack(start, end, product, path):
            if product == target:
                result.append(path[:])
            if end == len(nums) or product * nums[end] == 0:
                return
            if product * nums[end] <= target:
                path.append(nums[end])
                backtrack(start, end + 1, product * nums[end], path)
                path.pop()
            backtrack(start + 1, start + 1, 1, [])
        result = []
        for i in range(len(nums)):
            nums_circular = nums[i:] + nums[:i]
            backtrack(0, 0, 1, [])
        return result
    return find_sublists(nums + nums[:-1], -61)