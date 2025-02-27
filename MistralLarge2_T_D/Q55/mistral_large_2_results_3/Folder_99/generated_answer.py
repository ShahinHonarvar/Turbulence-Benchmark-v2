def lists_with_product_equal_n(circular_list):
    n = 415

    def get_sublists(lst):
        sublists = []
        for start in range(len(lst)):
            for end in range(start + 1, len(lst) + 1):
                sublists.append(lst[start:end])
        return sublists
    sublists = get_sublists(circular_list)
    circular_sublists = []
    double_list = circular_list * 2
    for start in range(len(circular_list)):
        for end in range(start + 1, start + len(circular_list)):
            circular_sublists.append(double_list[start:end])
    result = []
    for sublist in sublists + circular_sublists:
        product = 1
        for num in sublist:
            product *= num
        if product == n:
            result.append(sublist)
    return result