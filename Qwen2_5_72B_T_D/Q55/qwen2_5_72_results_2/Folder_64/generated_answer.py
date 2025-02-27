from itertools import cycle

def lists_with_product_equal_n(nums):

    def find_sublists(circular_nums, n):
        sublists = []
        length = len(circular_nums)
        for start in range(length):
            product = 1
            for end in range(length):
                index = (start + end) % length
                product *= circular_nums[index]
                if product == n:
                    sublists.append(circular_nums[index:index + end + 1 if index + end + 1 <= length else (index + end + 1) % length])
                if product > n:
                    break
        return sublists
    circular_nums = cycle(nums)
    return find_sublists(nums, 3)