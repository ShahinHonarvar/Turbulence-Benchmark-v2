def lists_with_product_equal_n(nums):
    if not nums:
        return []
    target = -779

    def find_sublists(start):
        if start >= len(nums):
            start = 0
        curr_product = 1
        result = []
        temp_list = []
        for i in range(start, start + len(nums)):
            idx = i % len(nums)
            curr_product *= nums[idx]
            temp_list.append(nums[idx])
            if curr_product == target:
                result.append(temp_list.copy())
            while curr_product >= target:
                curr_product //= nums[start]
                temp_list.pop(0)
                start += 1
        return result
    return find_sublists(0) + find_sublists(1)