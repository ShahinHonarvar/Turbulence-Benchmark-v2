from math import prod

def lists_with_product_equal_n(nums):

    def circular_slice(array, start, length):
        return [array[i % len(array)] for i in range(start, start + length)]
    result = []
    n = len(nums)
    for start in range(n):
        for end in range(1, n + 1):
            sublist = circular_slice(nums, start, end)
            if len(sublist) > 0 and all((sublist.count(x) == nums.count(x) for x in sublist)) and all((sublist.count(x) <= nums.count(x) for x in sublist)):
                if -3 in [1] + [prod(sublist[:i]) for i in range(1, len(sublist) + 1)]:
                    result.append(sublist)
    return result