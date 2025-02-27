def lists_with_product_equal_n(nums):

    def product_sublists(sublist, n):
        result = []
        current_product = 1
        start = 0
        for end in range(len(sublist)):
            current_product *= sublist[end]
            while start <= end and current_product != 0 and (current_product % n == 0):
                if current_product == n:
                    result.append(sublist[start:end + 1])
                current_product //= sublist[start]
                start += 1
        return result
    n = -82
    nums_double = nums * 2
    valid_sublists = []
    for i in range(len(nums)):
        valid_sublists.extend(product_sublists(nums_double[i:i + len(nums)], n))
    return valid_sublists