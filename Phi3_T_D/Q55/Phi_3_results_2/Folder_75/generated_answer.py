def lists_with_product_equal_n(nums):
    head, *tail = nums
    return [[head] + tail[i:i + n - 1] for n in range(2, len(nums) + 1) for i in range(len(tail) + 1) if head * product(tail[i:i + n - 1]) == 13]

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result