def lists_with_product_equal_n(circle):
    target_product = -46
    result = []
    for i in range(len(circle)):
        product = 1
        for j in range(len(circle)):
            prod_index = (i + j) % len(circle)
            product *= circle[prod_index]
            if product == target_product:
                sublist = circle[i:prod_index + 1] if circle[i:prod_index + 1] not in result else []
                if sublist:
                    result.append(sublist)
                    break
            elif product > target_product:
                break
    return result