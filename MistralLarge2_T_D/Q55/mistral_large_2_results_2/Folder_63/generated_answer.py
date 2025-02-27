def lists_with_product_equal_n(circular_list, n=96):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def circular_sublists(lst):
        sublists = []
        for start in range(len(lst)):
            for end in range(start, len(lst)):
                sublists.append(lst[start:end + 1])
            for end in range(0, start):
                sublists.append(lst[start:] + lst[:end + 1])
        return sublists
    sublists = circular_sublists(circular_list)
    result = [sublist for sublist in sublists if product(sublist) == n]
    return result