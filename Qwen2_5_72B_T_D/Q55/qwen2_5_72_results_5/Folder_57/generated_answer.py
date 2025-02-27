def lists_with_product_equal_n(nums):
    size = len(nums)
    found_sublists = []
    for i in range(size):
        product = 1
        for j in range(size):
            index = (i + j) % size
            product *= nums[index]
            if product == -75:
                found_sublists.append(nums[i:index + 1])
            elif product == 0:
                break
    return found_sublists