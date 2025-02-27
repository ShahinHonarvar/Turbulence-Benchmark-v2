def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current):
        result = []
        for i in range(start, start + len(nums)):
            product *= nums[i % len(nums)]
            current.append(nums[i % len(nums)])
            if product == -115:
                result.append(current[:])
            result += find_sublists(i + 1, product, current)
            current.pop()
            product /= nums[i % len(nums)]
        return result
    result = []
    for i in range(len(nums)):
        result += find_sublists(i, 1, [])
    return [r for r in result if len(r) <= len(nums) and (not any((r.count(x) > nums.count(x) for x in r)))]