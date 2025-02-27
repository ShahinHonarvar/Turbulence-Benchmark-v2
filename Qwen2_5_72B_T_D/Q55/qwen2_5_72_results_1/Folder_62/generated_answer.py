def lists_with_product_equal_n(nums):
    n = 100
    result = []
    length = len(nums)

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
            if product > n:
                return False
        return product == n
    for i in range(length):
        for j in range(1, length + 1):
            sublist = nums[i:i + j] + nums[:j - (length - i) % length]
            if check_product(sublist):
                result.append(sublist)
    return result