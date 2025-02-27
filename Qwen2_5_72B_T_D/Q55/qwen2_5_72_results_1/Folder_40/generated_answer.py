def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    def generate_sublists(start, length):
        sublists = []
        for i in range(length):
            end = (start + i) % length
            sublist = circular_list[start:end + 1] if start <= end else circular_list[start:] + circular_list[:end + 1]
            sublists.append(sublist)
        return sublists
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(1, length + 1):
            for sublist in generate_sublists(start, length):
                if product_of_sublist(sublist) == -9:
                    result.append(sublist)
    return result