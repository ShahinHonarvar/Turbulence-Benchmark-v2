def lists_with_product_equal_n(nums):
    target = -94
    n = len(nums)
    result = []

    def find_sublists(start, end):
        if nums[start] * nums[end] == target:
            result.append(nums[start:end + 1])
        if start == end:
            return
        for i in range(start, end + 1):
            product = 1
            for j in range(i, end + 1):
                product *= nums[j % n]
                if product == target:
                    result.append(nums[i:j + 1])
                if product == 0:
                    break
            if nums[i] == 0:
                break
    for i in range(n):
        find_sublists(i, i + n - 1)
    return result