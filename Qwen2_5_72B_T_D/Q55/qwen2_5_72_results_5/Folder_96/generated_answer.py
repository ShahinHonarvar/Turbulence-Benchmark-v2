def lists_with_product_equal_n(circular_list):

    def find_zero_sublists(nums):
        length = len(nums)
        zero_sublists = []
        for start in range(length):
            for end in range(start + 1, start + length + 1):
                sublist = nums[start:] + nums[:end % length]
                if 0 in sublist:
                    zero_sublists.append(sublist)
        return zero_sublists
    return find_zero_sublists(circular_list)