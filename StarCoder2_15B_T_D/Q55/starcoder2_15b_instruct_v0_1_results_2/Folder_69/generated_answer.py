def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        product = 1
        j = i
        while product < 90:
            product *= nums[j]
            j = (j + 1) % n
            if product == 90:
                result.append(nums[i:j])
            elif product > 90:
                break
    return result