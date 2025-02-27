def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    results = []

    def product(nums):
        total = 1
        for n in nums:
            total *= n
        return total

    def find_sublists(window_length):
        for i in range(size):
            sublist = circular_list[i:i + window_length]
            if len(sublist) == window_length:
                if product(sublist) == 8:
                    results.append(sublist)
            if i + window_length < size:
                sublist = circular_list[i:i + window_length] + circular_list[:window_length - (size - (i + window_length))]
                if product(sublist) == 8:
                    results.append(sublist)
            if i + window_length >= size:
                break
    for window_length in range(1, size + 1):
        find_sublists(window_length)
    return results