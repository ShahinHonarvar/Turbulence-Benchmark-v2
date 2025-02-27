def get_circular_products(nums, start, end):
    size = len(nums)
    while end != start:
        yield (nums[start] * nums[end])
        end = (end + 1) % size

def lists_with_product_equal_n(nums):
    results = []
    for i in range(len(nums)):
        found = False
        for j in range(i, i + len(nums)):
            current = get_circular_products(nums, i, j % len(nums))
            if any((prod == -16 for prod in current)):
                results.append(nums[i:j % len(nums) + 1])
                found = True
        if not found:
            break
    return results