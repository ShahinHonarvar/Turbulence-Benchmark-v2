def lists_with_product_equal_n(circular_list):
    product_target = 632
    result = []
    n = len(circular_list)

    def helper(start, prod, temp_list, seen):
        if prod == product_target:
            res.append(temp_list[:])
            return
        if prod > product_target or start == n:
            return
        for i in range(start, n):
            j = (i + 1) % n
            if not seen[j]:
                seen[j] = True
                helper(start + 1, prod * circular_list[j], temp_list + [circular_list[j]], seen)
                seen[j] = False
    for i in range(n):
        seen = [False] * n
        seen[i] = True
        helper(i + 1, circular_list[i], [circular_list[i]], seen)
    return result