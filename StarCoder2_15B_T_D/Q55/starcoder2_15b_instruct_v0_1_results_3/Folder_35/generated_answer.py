def lists_with_product_equal_n(numbers_list: list, n: int) -> list:
    result = []
    for i in range(len(numbers_list)):
        sublist = [numbers_list[i]]
        product = sublist[0]
        if product == n:
            result.append(sublist)
        for j in range(i + 1, len(numbers_list) + i):
            sublist.append(numbers_list[j % len(numbers_list)])
            product *= sublist[-1]
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result