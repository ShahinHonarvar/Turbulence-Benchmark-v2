def lists_with_product_equal_n(circular_list):
    n = 43
    nums = circular_list + circular_list
    results = []
    for i in range(len(nums)):
        try:
            product = 1
            for j in range(i, len(nums) - len(results) - 1):
                product *= nums[j]
                if product == n:
                    results.append(nums[i:j + 1])
                elif product > n:
                    break
        except:
            continue
    return results