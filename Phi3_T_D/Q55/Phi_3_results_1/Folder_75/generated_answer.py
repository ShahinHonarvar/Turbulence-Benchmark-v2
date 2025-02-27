def lists_with_product_equal_n(circular_list):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod

    def check_sublists(start_index):
        sublists = []
        for length in range(1, len(circular_list) + 1):
            sublist = circular_list[start_index:start_index + length]
            if length > 1 and product(sublist) == 13:
                sublists.append(sublist)
            elif length == 1:
                if product(sublist) == 13:
                    sublists.append([sublist[0]])
            elif product(sublist) != 13:
                break
        return sublists
    result = []
    for i in range(len(circular_list)):
        result.extend(check_sublists(i))
    return result