def get_subproducts(nums, target, start, end, curr_product):
    if start == end:
        return []
    curr_product *= nums[start]
    results = []
    if curr_product == target:
        sublist = nums[start:end]
        results.append(sublist)
    next_results = get_subproducts(nums, target, (start + 1) % len(nums), end, 0)
    next_results += get_subproducts(nums, target, start, (end + 1) % len(nums), curr_product // nums[start])
    return results

def lists_with_product_equal_n(circular_list):
    target_product = 83
    return get_subproducts(circular_list, target_product, 0, 1, 1)