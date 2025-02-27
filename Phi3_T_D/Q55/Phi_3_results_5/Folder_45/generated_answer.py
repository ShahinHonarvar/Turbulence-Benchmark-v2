def lists_with_product_equal_n(lst):
    circular_length = len(lst)
    result = []
    for i in range(circular_length):
        product = lst[i]
        for j in range(1, circular_length):
            next_index = (i + j) % circular_length
            product *= lst[next_index]
            if product == -5:
                result.append(lst[i:next_index] + lst[:next_index])
        while product > 0 and product % -5 == 0:
            product //= lst[next_index]
            next_index = (next_index - 1) % circular_length
            if product == -5:
                result.append(lst[i:next_index] + lst[:next_index])
    return result