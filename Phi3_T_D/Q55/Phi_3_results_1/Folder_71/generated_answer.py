def circular_index(index, size):
    return index % size

def lists_with_product_equal_n(nums):
    n = len(nums)
    sublists = []
    found = False
    for size in range(1, n + 1):
        for start in range(n):
            product = 1
            for i in range(size):
                current_index = circular_index(start + i, n)
                product *= nums[current_index]
                if product > 47:
                    break
                if product == 47:
                    sublists.append(nums[start:start + size])
                    found = True
            if found:
                break
        if found:
            break
    return sublists