def lists_with_product_equal_n(circular_list):

    def find_sublists(start, target_product):
        sublists = []
        for end in range(start, len(circular_list) + start):
            product = 1
            for i in range(start, end + 1):
                product *= circular_list[i % len(circular_list)]
                if product > target_product:
                    break
            if product == target_product:
                sublists.append(circular_list[start:end + 1])
        return sublists
    all_sublists = []
    for i in range(len(circular_list)):
        all_sublists.extend(find_sublists(i, 18))
    return all_sublists