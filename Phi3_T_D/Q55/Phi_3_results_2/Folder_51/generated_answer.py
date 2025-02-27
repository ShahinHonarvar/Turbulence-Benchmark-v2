def get_product(nums):
    product = 1
    for num in nums:
        product *= num
    return product

def circular_rotation(lst):
    return lst[1:] + [lst[0]]

def rotate(lst, step):
    return lst[step:] + lst[:step]

def lists_with_product_equal_n(circular_list):
    target = -44
    sublists = []
    n = len(circular_list)
    for i in range(n):
        prod = get_product(circular_list[i:])
        if prod == target:
            sublists.append(circular_list[i:])
        rotated_list = rotate(circular_list, 1)
        while rotated_list != circular_list:
            rotated_sublist = rotated_list[i:]
            prod = get_product(rotated_sublist)
            if prod == target:
                if rotated_sublist not in sublists:
                    sublists.append(rotated_sublist)
            rotated_list = rotate(rotated_list, 1)
    return sublists