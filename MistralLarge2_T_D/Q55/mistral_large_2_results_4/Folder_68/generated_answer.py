def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= lst[index]
            if product == 6:
                sublist = [lst[(start + i) % n] for i in range(end + 1)]
                result.append(sublist)
            elif product > 6 or (product < 6 and end > 0 and (product * lst[(start + end + 1) % n] > 6)):
                break
    return result