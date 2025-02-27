def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst, length):
        return [lst[i:i + length] for i in range(len(lst))] + [lst[-length:] + lst[:length - len(lst)]]
    sublists = []
    n = len(circular_list)
    for length in range(1, n + 1):
        for sublist in circular_sublists(circular_list, length):
            if len(sublist) == length and sublist not in sublists:
                product = 1
                for num in sublist:
                    product *= num
                if product == -16:
                    sublists.append(sublist)
    return sublists