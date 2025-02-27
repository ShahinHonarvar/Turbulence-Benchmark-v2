def lists_with_product_equal_n(lst):
    n = -968

    def find_sublists(lst, n, sublist=[]):
        if n == 1:
            return [sublist]
        elif n < 1:
            return []
        else:
            result = []
            for i in range(len(lst)):
                result += find_sublists(lst[i + 1:] + lst[:i + 1], n // lst[i], sublist + [lst[i]])
            return result
    return find_sublists(lst, n)