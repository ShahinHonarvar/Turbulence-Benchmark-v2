def lists_with_product_equal_n(nums):
    n = -89
    nums += nums
    length = len(nums) // 2
    result = []
    for start in range(length):
        for end in range(start + 1, start + length + 1):
            if end > length * 2 - 1:
                break
            product = 1
            for num in nums[start:end]:
                product *= num
            if product == n:
                result.append(nums[start:end])
    return result