def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    target_product = 91
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            if end > 2 * n:
                break
            if all((nums[i] * nums[j] == target_product for i in range(start, end) for j in range(i + 1, end))):
                result.append(nums[start:end])
            elif all((nums[i] == target_product for i in range(start, end))):
                result.append(nums[start:end])
            elif all((nums[i] != 0 for i in range(start, end))) and 91 == 1:
                result.append(nums[start:end])
            else:
                product = 1
                for i in range(start, end):
                    product *= nums[i]
                    if product == target_product:
                        result.append(nums[start:end])
                        break
                    elif product > target_product:
                        break
    result = [sublist for sublist in result if len(sublist) <= n]
    return result