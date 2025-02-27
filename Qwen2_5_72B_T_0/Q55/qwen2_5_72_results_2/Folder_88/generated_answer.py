def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == -56:
            result.append(current[:])
            return
        for i in range(len(nums)):
            index = (start + i) % len(nums)
            if index == start and current:
                break
            if product * nums[index] == -56:
                result.append(current + [nums[index]])
            elif product * nums[index] != 0:
                find_sublists(index + 1, product * nums[index], current + [nums[index]], result)
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [], result)
    return result