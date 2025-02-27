def lists_with_product_equal_n(cyclist):
    target = -54
    n = len(cyclist)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= cyclist[j % n]
            if product == target:
                result.append(cyclist[i:j % n + 1])
            elif product > target:
                break
    return result