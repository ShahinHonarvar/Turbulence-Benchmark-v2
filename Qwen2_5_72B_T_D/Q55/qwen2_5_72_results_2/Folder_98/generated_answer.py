def lists_with_product_equal_n(nums):

    def find_sublists(start, current_product, current_list, all_lists):
        if start == len(nums):
            return
        n = len(nums)
        for length in range(1, n + 1):
            current_product = 1
            for i in range(start, start + length):
                index = i % n
                current_product *= nums[index]
            if current_product == -1:
                sublist = [nums[(start + j) % n] for j in range(length)]
                all_lists.append(sublist)
            if len(current_list) < n:
                find_sublists(start + 1, current_product, current_list, all_lists)
    result = []
    find_sublists(0, 1, [], result)
    return result

def optimized_lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        current_product = 1
        for length in range(1, n + 1):
            current_product *= nums[(start + length - 1) % n]
            if current_product == -1:
                sublist = [nums[(start + i) % n] for i in range(length)]
                result.append(sublist)
            if current_product == 0:
                break
    return result