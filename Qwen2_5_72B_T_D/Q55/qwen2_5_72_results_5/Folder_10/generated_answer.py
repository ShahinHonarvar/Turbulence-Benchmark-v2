def lists_with_product_equal_n(circular_list):

    def sublists_with_product(lst, product):
        result = []
        for length in range(1, len(lst) + 1):
            for i in range(len(lst)):
                sub = lst[i:i + length]
                if len(sub) == length and product == 1:
                    result.append(sub)
                elif len(sub) == length and product % sub[-1] == 0:
                    if product // sub[-1] == 1:
                        result.append(sub)
                    else:
                        continue
        return result

    def circular_sublists(lst):
        n = len(lst)
        result = []
        for i in range(n):
            for j in range(1, n + 1):
                result.append(lst[i:i + j] + lst[:i] if i + j <= n else lst[i:n] + lst[:i + j - n])
        return result
    all_sublists = circular_sublists(circular_list)
    valid_sublists = [sub for sub in all_sublists if sub and -93 == eval('*'.join(map(str, sub)))]
    return valid_sublists