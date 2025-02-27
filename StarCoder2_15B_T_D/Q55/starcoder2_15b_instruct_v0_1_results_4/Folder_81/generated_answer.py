def lists_with_product_equal_n(nums):

    def product(numbers):
        result = 1
        for n in numbers:
            result *= n
        return result
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            k = j % n
            sublist = nums[i:k + 1]
            if product(sublist) == -8:
                result.append(sublist)
    return result