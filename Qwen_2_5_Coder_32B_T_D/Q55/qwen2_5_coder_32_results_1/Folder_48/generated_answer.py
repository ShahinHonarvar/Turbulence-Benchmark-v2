def lists_with_product_equal_n(lst):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(lst)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= lst[end % n]
            if current_product == 990:
                result.append(lst[start:end % n + 1])
            elif current_product > 990:
                break
    return result