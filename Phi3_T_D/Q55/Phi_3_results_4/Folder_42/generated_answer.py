def lists_with_product_equal_n(lst):
    circular_lists = [lst[i:i + len(lst)] for i in range(len(lst))]
    output = []
    for circular_list in circular_lists:
        for i in range(len(circular_list)):
            for j in range(i + 1, len(circular_list) + 1):
                sublist = circular_list[i:j]
                product = 1
                for num in sublist:
                    product *= num
                if product == 25:
                    output.append(sublist)
    return output