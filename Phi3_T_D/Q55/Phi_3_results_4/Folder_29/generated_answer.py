from itertools import cycle

def lists_with_product_equal_n(nums):

    def contiguous_sublist_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 15
    result = []
    circular_nums = cycle(nums)
    for start_index in range(len(nums)):
        for sublist_length in range(1, len(nums) + 1):
            sublist = [next(circular_nums) for _ in range(sublist_length)]
            if contiguous_sublist_product(sublist):
                result.append(sublist)
            if len(sublist) == len(nums):
                break
    return result