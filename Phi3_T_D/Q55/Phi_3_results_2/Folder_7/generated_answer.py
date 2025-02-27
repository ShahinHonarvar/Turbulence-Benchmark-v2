def lists_with_product_equal_n(nums):

    def get_next_index(index, size):
        return (index + 1) % size
    n = len(nums)
    target = 537
    found_sublists = []
    for start_index in range(n):
        product = 1
        for i in range(start_index, start_index + n):
            index = i % n
            product *= nums[index]
            if product == target:
                found_sublists.append(nums[start_index:index + 1])
            elif product > target:
                break
    return found_sublists