def lists_with_product_equal_n(circum_list, target_product=-837):

    def gen_circum_lists(lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                yield lst[i:j]
    list_of_sublists = [sublist for sublist in gen_circum_lists(circum_list) if (product := functools.reduce(lambda x, y: x * y, sublist)) == target_product]
    return list_of_sublists