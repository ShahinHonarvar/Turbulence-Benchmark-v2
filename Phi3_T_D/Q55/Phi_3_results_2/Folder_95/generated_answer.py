def product_of_list_elements(lst):
    product = 1
    for item in lst:
        product *= item
    return product

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    target_product = 28
    solutions = []
    for i in range(size):
        j = i
        sublist = []
        while j < size and j >= 0 and (sublist == [] or product_of_list_elements(sublist) * circular_list[j] == target_product):
            sublist.append(circular_list[j % size])
            if product_of_list_elements(sublist[1:]) == target_product:
                solutions.append(sublist[1:])
            j += 1
    return solutions