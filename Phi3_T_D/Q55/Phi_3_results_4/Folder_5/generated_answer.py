def circular_product_helper(nums, target):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        temp_list = []
        for j in range(n):
            product *= nums[(i + j) % n]
            temp_list.append(nums[(i + j) % n])
            if product == target:
                result.append(temp_list[:])
                break
            elif product > target:
                break
    return result

def lists_with_product_equal_n(circular_list):
    return circular_product_helper(circular_list, -33)